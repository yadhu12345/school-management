from django.urls import path
from smsapp import views as api_views
from rest_framework.authtoken import views
from user import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('login/', views.user_login, name='loginu'),
    path('logout/', views.user_logout, name='logoutu'),
    path('registration/', views.user_registration, name="registrationu"),
    path('home', views.home, name='homeu'),
    path('info', views.info, name='info'),
    path('results', views.getresult, name='resultu'),
]