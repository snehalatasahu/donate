from django.shortcuts import render
from .forms import DonorForm
from django.conf import settings
import razorpay
from .models import Donor

client =razorpay.Client(auth=(settings.RAZORPAY_PUBLIC_KEY,settings.RAZORPAY_SECRET_KEY))
client.set_app_details({"title" : "Django", "version" : "3.0.4"})
def create_bill(request):
    donor = Donor.objects.latest('id')
    if request.method == 'POST':
        payment_id=request.POST['razorpay_payment_id']
        print("Payment Id",payment_id)
        amount_in_paise = donor.get_amount()
        payment_client_capture=(client.payment.capture(payment_id,amount_in_paise))    
        print("Payment Client capture",payment_client_capture)
        payment_fetch=client.payment.fetch(payment_id)
        donor.paid = True
        donor.save()
        return render(request, 'bill.html', {'donor':donor, 'payment_id':payment_id})

    # return render(request, 'create_bill.html', {'donor':donor, 'public_key':settings.RAZORPAY_PUBLIC_KEY})

def home(request):
    form = DonorForm()
    if request.method == 'POST':
        donorForm = DonorForm(request.POST) 
        if donorForm.is_valid():
            donorForm.save(commit=True)
            donor = Donor.objects.latest('id')
            amount_in_paise = donor.get_amount()
            return render(request, 'create_bill.html', {'donor':donor, 'amount_in_paise':amount_in_paise, 'public_key':settings.RAZORPAY_PUBLIC_KEY})
  
    return render(request, 'index.html', {'form':form})