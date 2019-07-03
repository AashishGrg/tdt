from django.db import models
import datetime

class Order(models.Model):
    detail = models.CharField(max_length=250, blank=False)
    user = models.ForeignKey(   
        'authentication.User', on_delete=models.CASCADE, related_name='order_user')    
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('OnTheWay', 'OnTheWay'),
        ('Delivered','Delivered')
    )
    status = models.CharField(
        max_length=100, choices=ORDER_STATUS, default="Pending")
    order_date = models.DateTimeField(default=datetime.datetime.now())
    expected_date = models.DateTimeField(null=True)
    delivered_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.order_date