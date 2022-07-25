from django.urls import path
from task_manager.tasks.views import TasksListView, DetailedTaskView,\
    CreateTaskView, UpdateTaskView, DeleteTaskView

app_name = 'tasks'
urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete'),
    path('<int:pk>/', DetailedTaskView.as_view(), name='task_view'),
]
