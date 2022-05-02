from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Task, Categories
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

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('movies/', views.Movies.as_view(), name="movies"), 
    path('books/', views.Books.as_view(), name="books"),
    path('broadways/', views.Broadways.as_view(), name="broadways"),
    path('createList/', views.CreateList.as_view(), name="createList"),
    path('edit&deleteList/<int:pk>', views.EditDeleteList.as_view(), name="editDeleteList"),
    path('user/<username>', views.Profile, name="profile"),
    path('lists/<int:pk>', views.DetailListPage.as_view(), name="home"), 
    path('books/<int:pk>', views.DetailBookPage.as_view(), name="detailBook"),
    path('broadways/<int:pk>', views.DetailBroadwayPage.as_view(), name="detailBroadway"),
    path('movies/<int:pk>', views.DetailMoviePage.as_view(), name="detailMovie"),
    path('accounts/signup/', views.Signup, name='signup'),
]