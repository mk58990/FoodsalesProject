from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodDetails
from .serializer import FoodDetailsSr

# Create your views here.
class Food(APIView):
    def get(self,r):
        foodlist=FoodDetails.objects.all()
        serobj=FoodDetailsSr(foodlist,many=True)
        return Response(serobj.data)


    def post(self,r):
        serobj=FoodDetailsSr(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)