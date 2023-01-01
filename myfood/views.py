from django.http import request
from django.shortcuts import redirect, render
from .models import Item
from .forms import ItemForm
# Create your views here.
def index(request):
    items_list=Item.objects.all()
    context={
        'items_list':items_list
    }
    return render(request,'myfood/index.html',context)

def item(request):
    pass

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request,'myfood/detail.html',context)
    
    
def add_item(request):
    form=ItemForm(request.POST)
    
    
    if form.is_valid():
        form.save()
        return redirect('myfood:index')
    return render (request,'myfood/addItem-form.html',{'form':form})


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('myfood:index')
    return render(request,'myfood/addItem-form.html',{'form':form,'item':item})


def delete_item(request,id):
    item=Item.objects.get(id=id)
    
    if request.method=='POST':
        item.delete()
        return redirect('myfood:index')
    return render(request,'myfood/deleteItem.html',{'item':item})
    
    

    