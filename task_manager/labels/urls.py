from django.urls import path
from task_manager.labels.views import LabelsListView, CreateLabelView, \
    UpdateLabelView, DeleteLabelView


app_name = 'labels'
urlpatterns = [
    path('', LabelsListView.as_view(), name='labels'),
    path('create/', CreateLabelView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='delete'),
]
