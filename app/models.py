from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
   name = models.CharField(max_length = 5)
   phone_no = models.CharField(max_length = 10)
   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
   def __str__(self):
       return "{}".format(self.username)

# Create your models here.
class Service(models.Model):
    service_name = models.CharField("Service", max_length=255, default="<No name provided>")
    rate = models.IntegerField("Rate", default=0, blank=True, null=True)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)

    def __str__(self):
        return self.service_name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff")
    name = models.CharField("Staff Name", max_length=255, default="NULL", blank=False, null=False)
    contact = models.IntegerField("Contact Number", blank=True, null=True)
    salary = models.IntegerField("Salary", blank=True, null=True)
    password= models.CharField("Password", max_length=255, default="NULL", blank=False, null=False)
    date_created = models.DateTimeField("Date Joined", auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer_name = models.CharField("Customer Name", max_length=255, blank=True, null=True, default="Anonymous")
    contact = models.IntegerField("Contact Number", blank=True, null=True)
    is_repeat_customer = models.BooleanField("Repeat Customer", default=False)
    transaction_cost = models.IntegerField("Total Amount", null=True, default=0)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    serving_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="transactions")  # One-to-many relationship
    services = models.ManyToManyField(Service, related_name="transactions")  # Many-to-many relationship

    def __str__(self):
        return f"{self.date_created}_{self.customer_name}-{self.services.count()}"
