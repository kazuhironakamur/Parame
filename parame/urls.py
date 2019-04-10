from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/sheets', views.sheet_list, name='sheet_list'),
    path('<int:pk>/sheets/<int:sk>', views.sheet_detail, name='sheet_detail'),
]