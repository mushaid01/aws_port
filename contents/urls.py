from .import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
app_name='contents'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('certification/<int:pk>/', views.certification, name='certification'),
    path('project-document/<int:pk>/', views.project_document, name='project_document'),
    path('MIR_MUSHAIDUL_ISLAM_ER.pdf/', views.resume, name='resume'),
    path('seminar/<int:pk>/', views.seminar, name='seminar'),
    path('user_settings/', views.userSettings, name="user_settings"),
    path('update_theme/', views.updateTheme, name="update_theme"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
