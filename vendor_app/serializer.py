from rest_framework.serializers import ModelSerializer
from vendor_app.models import VendorInfo,OrderTracking
class VendorInfoSerializer(ModelSerializer):

    class Meta:
        model=VendorInfo
        fields= '__all__'

class OrderTrackingSerializer(ModelSerializer):

    class Meta:
        model=OrderTracking
        fields= '__all__'