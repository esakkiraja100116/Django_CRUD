from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import * 

urlpatterns = [
   path("",index,name='index'),
   path("add_fruit",add_fruit,name='add_fruit'),
   path("delete_fruit/<int:myid>/",delete_fruit,name='delete_fruit'),
   path("edit_fruit/<int:myid>/",edit_fruit,name='edit_fruit'),
]
 