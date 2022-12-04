from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    template_name= 'snack_list.html'
    model= Snack
    context_object_name="allThings"

class SnackDetailView(DetailView): 
    template_name= 'snack_detail.html'
    model= Snack

class SnackCreateView(CreateView):
    template_name= 'snack_create.html'
    model= Snack
    fields= ['name','purchaser','desc']

class SnackUpdateView(UpdateView):
    template_name= 'snack_update.html'
    model= Snack
    fields= ['name','purchaser','desc']
    success_url=reverse_lazy('thing_list')


class SnackDeleteView(DeleteView):
    template_name= 'snack_delete.html'
    model= Snack
    success_url=reverse_lazy('thing_list')