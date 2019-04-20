from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/new', views.project_new, name='project_new'),
    path('project/<int:pk>/edit', views.project_edit, name='project_edit'),
    path('<int:pk>/sheets', views.sheet_list, name='sheet_list'),
    path('<int:pk>/sheets/<int:sk>', views.sheet_detail, name='sheet_detail'),
    path('<int:pk>/sheets/<int:sk>/edit', views.sheet_edit, name='sheet_edit'),
]