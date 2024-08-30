import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import render

# Create your views here.
class SumaView(APIView):
    def get(self,request,*args,**kwargs):
        num_one=request.GET.get("num_one")
        num_two=request.GET.get("num_two")
        suma=int(num_one)+ int(num_two)
        return Response (suma, status= status.HTTP_200_OK)



class RestaView(APIView):
    def get(self,request,*args,**kwargs):
        num_one=request.GET.get("num_one")
        num_two=request.GET.get("num_two")
        resta=int(num_one)- int(num_two)
        return Response (resta, status= status.HTTP_200_OK)
    
class MultiplicacionView(APIView):
    def get(self,request,*args,**kwargs):
        num_one=request.GET.get("num_one")
        num_two=request.GET.get("num_two")
        multiplicacion=int(num_one)*int(num_two)
        return Response (multiplicacion, status= status.HTTP_200_OK)
    
class DivisionView(APIView):
    def get(self, request, *args, **kwargs):
        num_one = request.GET.get("num_one")
        num_two = request.GET.get("num_two")

       
        if num_one is not None and num_two is not None:
            try:
                num_one = float(num_one)
                num_two = float(num_two)

                
                if num_two == 0:
                    return Response({'error': 'No se puede dividir entre cero.'}, status=status.HTTP_400_BAD_REQUEST)

              
                division = num_one / num_two
                return Response({'resultado': division}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({'error': 'Entrada inválida. Proporcione números válidos.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Faltan parámetros. Proporcione num_one y num_two.'}, status=status.HTTP_400_BAD_REQUEST)
        