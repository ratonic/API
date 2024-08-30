from django.urls import path
from .views import SumaView
from .views import RestaView
from .views import MultiplicacionView
from .views import DivisionView

urlpatterns =[
    path("sumar",SumaView.as_view()),
    path("restar",RestaView.as_view()),
    path("multiplicar",MultiplicacionView.as_view()),
    path("dividir",DivisionView.as_view())



]