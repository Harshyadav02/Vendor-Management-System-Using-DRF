from django.contrib import admin
from django.urls import path,include
from vendor_app.views import (VendorProfileById,
                              VendorProfile,
                              PurchaseOrderTracking,
                              PurchaseOrderTrackingById,
                              )

urlpatterns = [
    
    # Vendor Profile Management
    path('api/vendors/',VendorProfile.as_view(),name='vendor_detail'),
    path('api/vendors/<int:vendor_id>/',VendorProfileById.as_view()),

    # Purchase Order Tracking
    path('api/purchase_orders/',PurchaseOrderTracking.as_view()),
    path('api/purchase_orders/<str:purchase_order_id>',PurchaseOrderTrackingById.as_view())

]