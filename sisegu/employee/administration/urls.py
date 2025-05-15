from django.urls import path
from sisegu.employee.administration import views

app_name='administration'

urlpatterns = [
    path('branch/', views.branches_index, name='branch_index'),
    path('members/', views.members_index, name='members_index'),
    path('outgoingmails/', views.outgoingmails_index, name='outgoingmails_index'),
    path('outgoingmails/add/', views.outgoingmails_add, name='outgoingmails_add'),
    path('outgoingmails/<int:id>', views.outgoingmails_detail, name='outgoingmails_detail'),
    path('incomingmails/', views.incomingmails_index, name='incomingmails_index'),
]
