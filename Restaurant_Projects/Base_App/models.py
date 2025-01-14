from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length =15)

    def __str__(self):
        return self.Category_name
    


class Item(models.Model):
   Item_name = models.CharField(max_length =20)
   description = models.TextField(blank=False)
   Price = models.IntegerField()
   Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
   Image = models.ImageField(upload_to='item/')

   def __str__(self):
        return self.Item_name

class About(models.Model):
    Description =models.TextField( blank=False)

class FeedBack(models.Model):
    User_Name =models.CharField(max_length=15)
    Description =models.TextField( blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='item/')

    def __str__(self):
        return self.User_Name


class Book_Table(models.Model):
    Name = models.CharField(max_length =15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date= models.DateField()

    def __str__(self):
        return self.Name

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    payment_method = models.CharField(
        max_length=50,
        choices=[('cash_on_delivery', 'Cash on Delivery'), ('online_payment', 'Online Payment')],
        default='cash_on_delivery',  # Set default value to 'cash_on_delivery'
    )
    

    def save(self, *args, **kwargs):
        # Calculate the total price before saving
        self.total_price = self.item.Price * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order by {self.customer_name} for {self.item.Item_name}"
    

