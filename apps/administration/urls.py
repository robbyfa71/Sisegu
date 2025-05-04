from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_index, name='branch_index'),
    path('members/', views.members_index, name='members_index')
]