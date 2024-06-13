from django.urls import path
from medapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('purchase',views.purchase,name='purchase'),
    path('checkout/',views.checkout,name='checkout'),
    path('contactus/',views.contactus,name='contactus'),

]
