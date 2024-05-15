from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from vendor_app.serializer import VendorInfoSerializer,OrderTrackingSerializer
from vendor_app.models import VendorInfo,OrderTracking

#   Vendor Profile Management

class VendorProfile(APIView):

    ''' get all vendor details '''
    def get(self,request):

        try :
            vendor_detail_queryset= VendorInfo.objects.all()
            serialized_vendor_data = VendorInfoSerializer(vendor_detail_queryset,many=True)
        except VendorInfo.DoesNotExist:
                return Response({'error' :'No Vendor exist'})
        return Response(serialized_vendor_data.data)
    
    ''' create a new vendor '''

    def post(self,request,*args,**kwargs):
        
        serialized_data = VendorInfoSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg' : "Vendor data saved successfully"})
        return Response(serialized_data.errors)
    
class VendorProfileById(APIView):
     
    '''get vendor details based on vendor id'''
    def get(self,request,vendor_id):
         
        try: 
            vendor_detail=VendorInfo.objects.get(vendor_id=vendor_id)
        except VendorInfo.DoesNotExist:
            return Response({'error':'Vendor does not exist'})
        
        serialized_vendor_data=VendorInfoSerializer(vendor_detail)
        return Response(serialized_vendor_data.data)
    
    '''update the vendor details based on vendor id '''
    def put(self,request,vendor_id,*args,**kwargs):

        try:
            vendor_detail=VendorInfo.objects.get(vendor_id=vendor_id)
            
        except VendorInfo.DoesNotExist:
            return Response({'error':'Vendor does not exist'})
        
        serialized_vendor_data=VendorInfoSerializer(vendor_detail,data=request.data)
        
        if serialized_vendor_data.is_valid():
            serialized_vendor_data.save()
            return Response({'msg':'vendor updated successfully'})
        
        return Response(serialized_vendor_data.errors)
    
    '''delete vendor '''
    def delete(self,request,vendor_id,*args,**kwargs):
        
        try:
            vendor_data = VendorInfo.objects.get(vendor_id=vendor_id)
        except VendorInfo.DoesNotExist:
            return Response({'error':'Vendor does not exist'})
        vendor_data.delete()
        return Response({'msg':'Vendor deleted successfully'})


# Purchase Order Tracking

class PurchaseOrderTracking(APIView):

    def get(self, request):
        
        # getting vender_id from query parameter to filter all the order based on vendor id
        vendor_id = request.query_params.get('vender_id')
        
        # Get all orders of a particular vendor based on vendor id
        if vendor_id:
            order_detail = OrderTracking.objects.filter(vender_reference_id=vendor_id)
            
            if not order_detail :
                return Response({'msg' : f'vendor id {vendor_id} has no order'})
        else:
            order_detail = OrderTracking.objects.all()
            
        serialized_order_data = OrderTrackingSerializer(order_detail, many=True)
        return Response(serialized_order_data.data)
    
    def post(self,request):

        serialized_data = OrderTrackingSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'order saved successfully'})
        return Response(serialized_data.errors)
    
class PurchaseOrderTrackingById(APIView):

    def get(self,request,purchase_order_id):

        try:
            order_detail=OrderTracking.objects.get(purchase_order_number=purchase_order_id)
        except OrderTracking.DoesNotExist:
            return Response({'msg':f'No order of order number {purchase_order_id}'})
        serialized_purchase_order_data_= OrderTrackingSerializer(order_detail)
        return Response(serialized_purchase_order_data_.data)
    
    def put(self,request,purchase_order_id):

        try:
            order_detail=OrderTracking.objects.get(purchase_order_number=purchase_order_id)
        except OrderTracking.DoesNotExist:
            return Response({'msg':f'No order of order number {purchase_order_id}'})
        
        serialized_purchase_order_data= OrderTrackingSerializer(order_detail,data=request.data)
        if serialized_purchase_order_data.is_valid():
            serialized_purchase_order_data.save()

            return Response({'msg':'Order detail updated succesfully'})
        return Response(serialized_purchase_order_data.errors)
    
    def delete(self,request,purchase_order_id):

        try:
            order_detail=OrderTracking.objects.get(purchase_order_number=purchase_order_id)
        except OrderTracking.DoesNotExist:
            return Response({'msg':f'No order of order number {purchase_order_id}'})
        order_detail.delete()
        return Response({'msg':'Order deleted successfully'})
