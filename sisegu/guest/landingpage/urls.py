from django.urls import path
from sisegu.guest.landingpage import views

app_name='landinng_page'

urlpatterns = [
    path('', views.index, name='index'),
]
