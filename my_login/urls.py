from django.urls import path
from my_login import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.resister, name='register'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('users', views.user_list, name="users")
]