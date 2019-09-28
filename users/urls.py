from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import login
from . import views

app_name = 'users'
urlpatterns = [
    # 登录界面  LoginView.as_view后面要加上()
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    #注销
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]