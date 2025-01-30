from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    
    path('service/add', ServiceCreateView.as_view(), name="add_service"),
    path('service/list', ServiceListView.as_view(), name="service_list"),

    path('staff/add', StaffCreateView.as_view(), name="add_staff"),
    path('staff/list', StaffListView.as_view(), name="staff_list"),

    path('transaction/new', TransactionCreateView.as_view(), name="new_transaction"),
    path('transaction/list', TransactionListView.as_view(), name="transaction_list")
]