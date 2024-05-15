from django.db import models 
import uuid
# Create your models here.

class VendorInfo(models.Model):
    
    vendor_code = models.IntegerField(primary_key=True,)
    name=models.CharField(max_length=20,null=False)
    contact_details = models.BigIntegerField(null=False)
    address = models.CharField(max_length=200,null=False)
    on_time_delivery_rate=models.FloatField(null=False)
    average_response_time=models.FloatField(null=False)
    quality_rating_avg=models.FloatField(null=False)
    fulfillment_rate=models.FloatField(null=False)

class PurchaseOrder(models.Model) :
    
    STATUS_CHOICES =(

        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Delivered' ,'Delivered'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending'),
    )

    purchase_order_number=models.CharField(primary_key=True,max_length=200,default=uuid.uuid4)
    vender_reference=models.ForeignKey(VendorInfo,on_delete=models.CASCADE,null=False,to_field='vendor_code')
    order_date=models.DateTimeField(null=False)
    delivery_date=models.DateTimeField(null=False)
    items=models.JSONField()
    items_quantity=models.IntegerField(null=False)
    quality_rating=models.IntegerField(null=True)
    issue_date=models.DateTimeField(null=False)
    acknowledgment_date=models.DateField(null=False)
    status=models.CharField(choices=STATUS_CHOICES,max_length=100,null=False)