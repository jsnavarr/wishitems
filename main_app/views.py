from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Item

class ItemList(ListView):
  model = Item

def home(request):
    print('hi')
    item_list = Item.objects.all()
    print(item_list)
    return render(request, 'home.html', {'item_list': item_list})

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
#   fields = ['description']
#   def form_valid(self, form):
#     return super().form_valid(form)  
  success_url = '/'

def item_delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return redirect('items_index')
