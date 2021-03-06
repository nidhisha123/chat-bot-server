"""chatbot_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import chat, logout_user
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^chat/$', chat, name='chat'),
    url(r'^admin/', admin.site.urls),
    url(r'^'+'', include('chat_report.urls')),
    url(r'^login/', auth_views.LoginView.as_view(template_name='chatbot_tutorial/login.html'),name='login'),
    url(r'^logout/$', logout_user,name='logout'),
    # include("chatbot_tutorial.sub_routing.websocket_routing"),
    # include("chatbot_tutorial.sub_routing.custom_routing"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)