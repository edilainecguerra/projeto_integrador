from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('new/', views.new_task, name='new_task'),
    path('timer/', views.focus_timer, name='focus_timer'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]