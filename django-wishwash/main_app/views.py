#from .models import (models name here)
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response 
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import List, Book
import requests
import json

class Home(TemplateView):
    template_name = "home.html"

class Movies(TemplateView):
    template_name = "movies.html"
    response = requests.get("https://imdb-api.com/en/API/Top250Movies/k_lblhnjr6")
    print(response.status_code)
    print(response.json())
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    jprint(response.json())


class Books(TemplateView):
    template_name = "books.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['books'] = Book.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context['books'] = Book.objects.all()
            context['header'] = 'All Books'
        return context

class Broadways(TemplateView):
    template_name = "broadways.html"

class CreateList(LoginRequiredMixin, CreateView):
    template_name = "createList.html"

class EditDeleteList(UpdateView, DeleteView):
    template_name = "editDeleteList.html"

class DetailListPage(DetailView):
    template_name = "detailList.html"

class DetailBookPage(DetailView):
    model = Book
    template_name = "detailBook.html"

class DetailBroadwayPage(DetailView):
    template_name = "detailBroadway.html"

class DetailMoviePage(DetailView):
    template_name = "detailMovie.html"

def Profile(request, username):
    user = User.objects.get(username=username)
    list = List.objects.all()
    return render(request, 'profile.html',{'username':username, 'list':list})
    
def Signup(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/' + str(user.username))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})