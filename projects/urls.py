from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('main/', views.mainPage, name="main"),
    path('login/', views.LoginPage, name='login'),
    path('', views.SignupPage, name='signup'),
    path('projects/', views.projects, name="projects"),
    path('logout/', views.LogoutPage, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
