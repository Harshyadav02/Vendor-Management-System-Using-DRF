from rest_framework.serializers import ModelSerializer
from vendor_app.models import VendorInfo,PurchaseOrder
class VendorInfoSerializer(ModelSerializer):

    class Meta:
        model=VendorInfo
        fields= '__all__'

class OrderTrackingSerializer(ModelSerializer):

    class Meta:
        model=PurchaseOrder
        fields= '__all__'
