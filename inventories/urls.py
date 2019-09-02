
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='inventories'


urlpatterns = [
    path('list/', views.inventory_list, name= 'list')
    
    ]
