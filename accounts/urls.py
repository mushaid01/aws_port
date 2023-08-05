from importlib.resources import path
import re
from unicodedata import name
from django.contrib.auth import views as auth_views
#from django.conf.urls import url
from django.urls import re_path
from .import views
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.conf.urls.static import static
from django.conf import settings
app_name='accounts'

urlpatterns = [
    re_path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    re_path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    re_path('signup/',views.SignUp.as_view(),name='signup')    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
