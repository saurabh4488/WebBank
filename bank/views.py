from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, request
from .models import *


def index(request):
    return render(request,"home.html")

def Customer_Table(request):
    customers = Customer.objects.all()
    return render(request,"Customer.html",{'customers':customers})

def Trans(request,Acc):
    custom=Customer.objects.filter(Acc_No=Acc)
    context={'custom':custom,'Acc_No':Acc}
    return render(request, 'Transaction.html',context)

def Update_bal(request):
    customer=Customer.objects.all()
    recv_AccNo=int(request.POST.get('recv_AccNo'))
    Amt_to_transfer=int(request.POST.get('Amt_to_transfer'))
    upt=Customer.objects.filter(Acc_No=recv_AccNo)
    for x in upt:
        recv_curr_bal=x.Current_Balance

    #Sender's Details 
    sender_acc_no=int(request.POST.get('sender_acc_no'))
    update=Customer.objects.filter(Acc_No=sender_acc_no)
    if(sender_acc_no!=recv_AccNo && Amt_to_transfer!=0):
        flag1=0
        for y in update:
            sender_curr_bal=y.Current_Balance

            flag=0

            send_debit=sender_curr_bal-Amt_to_transfer

        if send_debit<0:
            flag=1
            custom=Customer.objects.filter(Acc_No=sender_acc_no)
            context={'flag':flag,'custom':custom,'Acc_No':sender_acc_no}
            return render(request,"Transaction.html",context)

        else:
            recv_credit=recv_curr_bal+Amt_to_transfer
            for a in update:
                a.Current_Balance=send_debit
                send_name=a.Account_Holder
                a.save()
        
            for p in upt:
                p.Current_Balance=recv_credit
                recv_name=p.Account_Holder
                p.save()

                sender=Customer.objects.get(Acc_No=sender_acc_no)
                tran=Transaction.objects.create(Acc_No=sender, Amount_transferred= Amt_to_transfer, Acc_no_of_reciever=recv_AccNo, updated_balance_of_reciever=recv_credit, Updated_balance_of_sender=send_debit ,Sender_name=send_name ,Reciever_name=recv_name)

            customers = Customer.objects.all()
            context={'flag':flag, 'customers':customers}
            return render(request, "Customer.html",context)
    else:
        flag1=1
        custom=Customer.objects.filter(Acc_No=sender_acc_no)
        context={'flag1':flag1,'custom':custom,'Acc_No':sender_acc_no}
        return render(request,"Transaction.html",context)

    
def Transaction_His(request):
    transfer=Transaction.objects.all().order_by("-id")
    return render(request,"Transhis.html",{'transfer':transfer})    
    




    