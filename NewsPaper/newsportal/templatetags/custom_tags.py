from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag()
def current_time(format_string='%d %b %Y - %H:%M:%S'):
    return datetime.now().astimezone().strftime(format_string)