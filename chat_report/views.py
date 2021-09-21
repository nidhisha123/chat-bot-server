from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from .models import ChatJokesCounts, ChatCunsumerJokesCounts

# Create your views here.

@method_decorator(permission_required('chat_report.view_chatjokescounts'), name='dispatch')
@method_decorator(login_required, name='dispatch')
class JokesCount(ListView):
	model = ChatJokesCounts
	template_name = 'chat_report/table.html'
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['headers'] = {
			'joke' : 'Joke',
			'count' : 'Count'
		}
		context['label'] = 'Jokes Count'
		context['style_title'] = {'joke'}
		context['current_tabs'] = 'jokes_count'
		return context

@method_decorator(login_required, name='dispatch')
class ConsumerJokesCount(ListView):
	model = ChatCunsumerJokesCounts
	template_name = 'chat_report/table.html'
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['headers'] = {
			'user' : 'User',
			'joke' : 'Joke',
			'count' : 'Count'
		}
		context['label'] = 'Consumer Jokes Count'
		context['style_title'] = {'joke'}
		return context

	def get_queryset(self):
		filter_args = {}
		if not self.request.user.is_staff:
			filter_args['user'] = self.request.user.username
		return super().get_queryset().filter(**filter_args).order_by('-pk')
