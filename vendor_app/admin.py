from django.contrib import admin
from vendor_app.models import VendorInfo,PurchaseOrder

class AdminVendorInfo(admin.ModelAdmin) :
    list_display = ['vendor_code','name','contact_details','address','on_time_delivery_rate','average_response_time','quality_rating_avg','fulfillment_rate']

class AdminOrderTracking(admin.ModelAdmin):
    list_display=['purchase_order_number','vender_reference','order_date','delivery_date','items','items_quantity','quality_rating','issue_date','acknowledgment_date','status']

admin.site.register(VendorInfo,AdminVendorInfo)
admin.site.register(PurchaseOrder,AdminOrderTracking)
