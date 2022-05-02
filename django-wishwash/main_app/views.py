from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
#from .models import (models name here)
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
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

class Home(TemplateView):
    template_name = "home.html"

class Movies(TemplateView):
    template_name = "movies.html"

class Books(TemplateView):
    template_name = "books.html"

class Broadways(TemplateView):
    template_name = "broadways.html"

class CreateList(LoginRequiredMixin, CreateView):
    template_name = "createList.html"

class EditDeleteList(UpdateView, DeleteView):
    template_name = "editDeleteList.html"

class DetailListPage(DetailView):
    template_name = "detailList.html"

class DetailBookPage(DetailView):
    template_name = "detailBook.html"

class DetailBroadwayPage(DetailView):
    template_name = "detailBroadway.html"

class DetailMoviePage(DetailView):
    template_name = "detailMovie.html"

def Profile(request, username):
    template_name = "profile.html"
    
def Signup(request):
    template_name = "signup.html"