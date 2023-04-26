from TreeMenu.models import TreeMenu
from django import template
from django.http import HttpRequest
from django.shortcuts import reverse, NoReverseMatch

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, name: str = '', parent: int = 0):
    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:

        # Get path if request exist
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''

        data = TreeMenu.objects.select_related() \
            .filter(category__name=name) \
            .order_by('pk')

        menu = []

        for item in data:

            try:
                url = reverse(item.path)
            except NoReverseMatch:
                url = item.path

            menu.append({
                'id': item.pk,
                'url': url,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == current_path or current_path.rstrip('/') == url else False,
            })

    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
