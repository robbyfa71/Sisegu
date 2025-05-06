from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.index_view, name='dashboard'),
    path('logout', views.logout_view, name='logout')
]
