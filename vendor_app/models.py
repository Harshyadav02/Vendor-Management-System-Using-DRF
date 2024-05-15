from django.db import models 
import uuid
# Create your models here.

class VendorInfo(models.Model):
    
    vendor_id = models.IntegerField(primary_key=True,)
    vendor_name=models.CharField(max_length=20,null=False)
    vendor_contact = models.BigIntegerField(null=False)
    vendor_address = models.CharField(max_length=200,null=False)

class OrderTracking(models.Model) :
    STATUS_CHOICES =(

        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Delivered' ,'Delivered'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending'),
    )
    purchase_order_number=models.CharField(primary_key=True,max_length=200,default=uuid.uuid4)
    vender_reference=models.ForeignKey(VendorInfo,on_delete=models.CASCADE,null=False,to_field='vendor_id')
    order_date=models.DateField(null=False)
    items_quantity=models.IntegerField(null=False)
    status=models.CharField(choices=STATUS_CHOICES,max_length=100,null=False)