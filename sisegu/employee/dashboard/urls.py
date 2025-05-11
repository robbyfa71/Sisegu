from django.urls import path
from sisegu.employee.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.index_view, name='index'),
    path('logout', views.logout_view, name='logout')
]
