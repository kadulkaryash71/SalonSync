from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import datetime

from .forms import *
from .models import *

# Create your views here.
    
# Service Views
class ServiceListView(ListView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/service_list.html'
    context_object_name = 'services'

    def get(self, request):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services, 'form': self.form_class})

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/create_service.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
    context_object_name = 'service'

# Transaction Views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        return super().get_queryset().filter(date_created__gte=yesterday).order_by('date_created')

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/create_transaction.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['staff'] = Staff.objects.all()
        return context

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction_form.html'
    success_url = reverse_lazy('new_transaction')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction_confirm_delete.html'
    success_url = reverse_lazy('new_transaction')
    context_object_name = 'transaction'

# Staff Views
# List all staff members
class StaffListView(ListView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff/staff_list.html'  # Template to render the list
    context_object_name = 'staff_list'  # Name of the variable in the template

    def get(self, request):
        staff = Staff.objects.all()
        return render(request, self.template_name, {'staff': staff, 'form': self.form_class})
        

# Create a new staff member
class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff/create_staff.html'  # Template for the form
    success_url = reverse_lazy('staff_list')  # Redirect after successful creation

# Update an existing staff member
class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff_form.html'  # Template for the form
    success_url = reverse_lazy('staff_list')  # Redirect after successful update

# Delete a staff member
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff_confirm_delete.html'  # Template for confirmation
    success_url = reverse_lazy('staff_list')  # Redirect after successful deletion

# Function-based views
def index(request):
    return render(request, 'index.html')