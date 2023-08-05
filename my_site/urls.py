"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
# from django.conf.urls import url

from django.conf import settings

from django.views.static import serve

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin_mirmushaid/', admin.site.urls),
    path('blog/',include('blog.urls',namespace='blog')),
    path('todo_app/',include('todo_app.urls',namespace='todo_app')),
    path('',include("contents.urls",namespace='contents')),
    path('',include('accounts.urls',namespace='accounts')),
    path('',include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
