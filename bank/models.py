from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class Customer(models.Model):
    Acc_No = models.IntegerField(max_length=200, primary_key=True)
    Account_Holder = models.CharField(max_length=200)
    Email_Id = models.EmailField(max_length=200)
    Current_Balance=models.IntegerField(max_length=200)
    def __str__(self):
        return str(self.Acc_No)

   


class Transaction(models.Model):
    Acc_No=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Amount_transferred = models.IntegerField(default=0)
    Acc_no_of_reciever = models.IntegerField(default=0)
    updated_balance_of_reciever= models.IntegerField(default=0)
    Updated_balance_of_sender= models.IntegerField(default=0)
    Sender_name=models.CharField(max_length=100)
    Reciever_name=models.CharField(max_length=100)
    Date_Time=models.DateTimeField(default= timezone.now)

    

  

