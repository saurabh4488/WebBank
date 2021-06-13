from bank.models import Transaction
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Customer/',views.Customer_Table, name='Customer'),
    path('<int:Acc>/',views.Trans,name='Trans'),
    path('Transhis/',views.Update_bal, name='Transhis'),
    path('Trans_History/',views.Transaction_His,name='Transactions'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)