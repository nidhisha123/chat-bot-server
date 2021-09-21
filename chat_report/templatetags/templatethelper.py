from django import template
register = template.Library()

@register.filter
def getattribute(value, arg):
	"""Gets an attribute of an object dynamically from a string name"""
	try:
		if str(arg) in value:
			return value[str(arg)]
	except:
		if hasattr(value,str(arg)):
			return getattr(value,str(arg))
	return ''

@register.simple_tag
def page_url(value, key):
	return f'?{key}={value}'