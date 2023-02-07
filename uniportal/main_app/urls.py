from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.user_login, name='user_login'),
    path("login/", views.user_login, name='user_login'),
    path("logout/", views.user_logout, name='user_logout'),
    path('stu_dashboard/', views.stu_dashboard_view, name='stu_dashboard'),
    path('hod_dashboard/', views.hod_dashboard_view, name='hod_dashboard'),
    path('tea_dashboard/', views.tea_dashboard_view, name='tea_dashboard'),
    path("uploadfile/", views.upload_file, name='uploadfile'),
    path("plot/", views.plot_view, name='plot'),

]
