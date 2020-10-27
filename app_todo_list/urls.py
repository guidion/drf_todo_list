"""
AppTodoList URL Configuration
"""
from django.urls import path, re_path
from app_todo_list.views import TasksList, TaskDetail

app_name = 'app_todo_list'
urlpatterns = [
  re_path(r'^tasks/$', TasksList.as_view()),
  re_path(r'^tasks/(?P<pk>\d+)$', TaskDetail.as_view()),
]
