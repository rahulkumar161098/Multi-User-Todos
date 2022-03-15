"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='gest'),
    path('register/', views.reg, name='register_page'),
    path('login/', views.user_login, name='login_page'),
    path('logout/', views.logout_view, name='log_out'),
    path('user/', views.user_board, name='user_dashboard'),
    path('addTodos/', views.addTodos, name='addtodos'),
    path('delete/<int:id>', views.delete, name='todo_delete'),
    path('details/<int:id>', views.todoDetails, name='details'),
    path('edit/<int:id>', views.edit)
]
