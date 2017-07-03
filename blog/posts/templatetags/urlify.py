try:
    from urllib import quote_plus  # Python 2.X
except ImportError:
    from urllib.parse import quote_plus  # Python 3+

from django import template

register = template.Library()

@register.filter
def urlify(value):
	return quote_plus(value) 
