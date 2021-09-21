from django.conf import settings

# context processor to get settings
def global_settings(request):
	context = {
		'settings' : settings
	}
	return context