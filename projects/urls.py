from django.urls import path
from . import views

urlpatterns=[
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('createproject/',views.createproject,name= 'create-project'),
    path('updateproject/<str:pk>/',views.updateproject,name= 'update-project'),
    path('deleteproject/<str:pk>/',views.deleteproject,name= 'delete-project'),
    ]