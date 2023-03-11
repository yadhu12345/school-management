from django.urls import path
from smsapp import views as api_views
from rest_framework.authtoken import views
from smsapp import views
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('registration/', views.admin_registration, name="registration"),
    path('home/', api_views.home, name="home"),
    path('subject/', api_views.subjectView, name="subject"),
    path('staff/', api_views.staffinfoView, name="staff"),
    path('studentlogin/', api_views.studentloginView, name="studentlogin"),
    path('deletesl/', views.delete_data_studentl, name='deletesl'),
    path('student/', api_views.studentinfoView, name="student"),
    path('deletest/', views.delete_data_student, name='deletest'),
    path('result/', api_views.addresultView, name="result"),

]