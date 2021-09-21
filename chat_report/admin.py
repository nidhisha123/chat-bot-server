from django.contrib import admin

# Register your models here.
from chat_report.models import ChatJokesCounts, ChatCunsumerJokesCounts

admin.site.register(ChatJokesCounts)
admin.site.register(ChatCunsumerJokesCounts)