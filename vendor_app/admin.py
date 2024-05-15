from django.contrib import admin
from vendor_app.models import VendorInfo,OrderTracking

class AdminVendorInfo(admin.ModelAdmin) :
    list_display = ['vendor_id','vendor_name','vendor_contact','vendor_address']

class AdminOrderTracking(admin.ModelAdmin):
    list_display=['purchase_order_number','vender_reference','order_date','items_quantity','status',]

admin.site.register(VendorInfo,AdminVendorInfo)
admin.site.register(OrderTracking,AdminOrderTracking)
