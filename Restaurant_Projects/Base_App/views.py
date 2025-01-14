from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from Base_App.models import Book_Table,About, ItemList, Item, FeedBack
from Base_App.models import Book_Table
from django.contrib import messages
from django.core.exceptions import ValidationError
from Base_App.forms import OrderForm
from Base_App.models import Order



# Create your views here.

def HomeView(request):
  item = Item.objects.all()
  list = ItemList.objects.all()
  review = FeedBack.objects.all()
  return render(request,'home.html',{'item':item, 'list':list, 'review':review})

def AboutView(request):
  data = About.objects.all()
  return render(request,'about.html',{'data':data})

def MenuView(request):
  item = Item.objects.all()
  list = ItemList.objects.all()
  return render(request,'menu.html',{'item':item, 'list':list})

def BookTableView(request):
  if request.method == 'POST':
    name = request.POST.get('user_name')
    phone_number = request.POST.get('phone_number')
    user_email = request.POST.get('user_email')
    total_person = request.POST.get('total_person')
    booking_date = request.POST.get('booking_date')

    if name != '' and len(phone_number) == 10 and  user_email != '' and total_person != 0 and booking_date != '':
      data = Book_Table( Name=name,Phone_number=phone_number,Email=user_email, Total_person=total_person, Booking_date=booking_date)
      data.save()

        # Add success message
      messages.success(request, "Your table has been booked successfully!")
      return redirect('Book_Table')  # Replace 'book_table' with the name of your URL pattern
    else:
            # Add error message
      messages.error(request, "Failed to book the table. Please check your input and try again.")

  return render(request,'book-table.html')


def order_now(request):
    item_id = request.GET.get('item_id')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save order data along with selected payment method
            order = form.save(commit=False)
            order.payment_method = request.POST.get('payment_method')  # Get payment method from form
            order.save()
            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'order_now.html', {'form': form})

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_success.html', {'order': order})
    

   