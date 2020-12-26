from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, City, Vanue
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

def load_cities(request):
    country_id = request.GET.get('country')    
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context = {'cities': cities}
    return render(request, 'hr/city_dropdown_list_options.html', context)

def load_vanues(request):
    city_id = request.GET.get('city')    
    vanues = Vanue.objects.filter(city_id=city_id).order_by('name')
    context = {'vanues': vanues}
    return render(request, 'hr/vanue_ddl.html', context)