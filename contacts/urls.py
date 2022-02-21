from django.urls import path
from .import views

urlpatterns =[
    path('contactdetails/',views.home),
    path('contactdetails/addcontact',views.addcontact),
    path('contactdetails/displaycontact',views.displaycontact),
    path('contactdetails/deletecontact',views.deletecontact),
    path('contactdetails/updatecontact',views.updatecontact)
]