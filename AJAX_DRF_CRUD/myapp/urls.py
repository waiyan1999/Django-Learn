from django.urls import path
from myapp import views

urlpatterns = [
    
    #API 
    path('task/',views.TaskView.as_view(),name='task'),
    path('task-detail/<int:pk>/',views.TaskDetailView.as_view(),name='task_detail'),
    
    #Query
    path('',views.Index.as_view(),name='index')
    
]