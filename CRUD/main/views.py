from email import message
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    
    context = {
        'item_list' : Item.objects.all()
    }

    # return HttpResponse("This is the index page")
    return render(request,'index.html',context)

def add_fruit(request):
    
    if request.method == "POST":
        fruit_name = request.POST['fruit_name']
        item = request.POST['item']

        item = Item(fruit_name = fruit_name,item = item)
        item.save()
        messages.info(request,"Item added successfully")

        item_list = Item.objects.all()
        context = {
            'item_list' : item_list
        }

        return render(request,'index.html',context)

        # return render(request,'index.html')
    else:
        pass


    return render(request,'add_fruit.html')


def delete_fruit(request,myid):
    fruit = get_object_or_404(Item, id=myid)
    fruit.delete()
    messages.info(request,"Fruit deleted successfully")
    return redirect(index)


def edit_fruit(request,myid):
    if request.method == "POST":
        item = Item.objects.get(id=myid)
        item.fruit_name = request.POST['fruit_name']
        item.item = request.POST['item']
        item.save()
        messages.info(request,"Fruit updated successfully")
        return redirect(index)

    else:

        fruit = get_object_or_404(Item,id=myid)
        context = {
            'fruit' : fruit
        }

        return render(request,'edit_fruit.html',context)
    