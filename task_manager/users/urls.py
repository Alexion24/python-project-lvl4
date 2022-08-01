from django.urls import path
from task_manager.users.views import UserListView, CreateUserView,\
    UpdateUserView, DeleteUserView


app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete'),
]
