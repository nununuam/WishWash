from dataclasses import field
from .models import Book, Movie, Play
#from calendar import calender
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
    response = requests.get("https://imdb-api.com/en/API/Top250Movies/k_lblhnjr6")
    #
    #print(response.status_code)
    #print(response.json())
    #def jprint(obj):
     #   text = json.dumps(obj, sort_keys=True, indent=4)
      #  print(text)
       # return text
    #jprint(response.json())

    #def gprint(text):
     #   array1 = text[1]
      #  print(array1 + "hello")

class Movies(TemplateView):
    template_name = "movies.html"
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         title = self.request.GET.get("title")
         context["movies"] = Movie.objects.all()
         return context

#API testing codes below
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #name = self.request.GET.get('moviename')
        #if name != None:
        #print(name)
        #response = requests.get(f'https://imdb-api.com/en/API/Search/k_lblhnjr6/{name}')
        #print(response.status_code)
        #print(response.json())
        #def jprint(obj):
            #text = json.dumps(obj, sort_keys=True, indent=4)
            #print(text)
            #return text
        #jprint(response.json())
        #with open(response.json()) as response:
            #data = json.load(response)
            #print(data)
           # context['movies'] = response.json()
            #context['header'] = f'Searching for {name}'
        #else:
         #   response2 = requests.get("https://imdb-api.com/en/API/Top250Movies/k_lblhnjr6")
          #  context['movies'] = response2.json()
           # context['header'] = 'Top 250 Movies'
        #return context
        
    
class Books(TemplateView):
    template_name = "books.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('title')
        if name != None:
            context['books'] = Book.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context['books'] = Book.objects.all()
            context['header'] = 'All Books'
        return context
#APIs Testing code below
    # url = 'http://openlibrary.org/search.json?'
    # response = requests.get(url)
    # data = response.text
    # parse_json = json.loads(data)
    # # print(response.status_code)
    
    # print(data)
    

class Broadways(TemplateView):
    template_name = "broadways.html"
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         title = self.request.GET.get("title")
         context["plays"] = Play.objects.all()
         return context

class CreateList(LoginRequiredMixin, CreateView):
    template_name = "createList.html"

# class EditList(UpdateView):
#     template_name = "editDeleteList.html"

# class delete list

class DetailListPage(DetailView):
    template_name = "detailList.html"

class DetailBookPage(DetailView):
    model = Book
    template_name = "detailBook.html"

# def DetailBookPage(request, book_id):
#     book = Book.objects.get(id=book_id)
#     return render(request, 'detailBook.html', {'book':book})
    

# def DetailBroadwayPage(request, play_id):
#     play = Play.objects.get(id=play_id)
#     return render(request, 'detailBroadway.html', {'play':play})
    
class DetailBroadwayPage(DetailView):
    model = Play
    template_name = "detailBroadway.html"
# def DetailMoviePage(request, movie_id):
#     movie = Movie.objects.get(id=movie_id)
#     return render(request, 'detailMovie.html', {'movie':movie})
class DetailMoviePage(DetailView):
    model = Movie
    template_name = "detailMovie.html"
    

class AddBook(LoginRequiredMixin, CreateView):
    template_name = "addbook.html"
    model = Book
    fields = '__all__'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/books')

class AddMovie(CreateView):
    # template_name = "addmovie.html"
    # model = Movie
    # fields = ['title', 'img', 'cast', 'trailer', 'book', 'plays']
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect('/movies')

    model = Movie
    fields = '__all__'
    template_name = "addmovie.html"
    success_url = '/movies/'

class AddPlay(CreateView):
    # template_name = "addplay.html" 
    # model = Play
    # fields = ['title', 'img', 'director', 'cast', 'book', 'movie']
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect('/broadways')
    model = Play
    fields = '__all__'
    template_name = "addplay.html"
    success_url = '/broadways/'

class MovieDelete(DeleteView):
    model = Movie
    template_name = 'moviedelete.html'
    success_url = "/movies/"

class BookDelete(DeleteView):
    model = Book
    template_name = 'bookdelete.html'
    success_url = "/books/"

class BroadwayDelete(DeleteView):
    model = Play
    template_name = 'broadwaydelete.html'
    success_url = "/broadways/"

class MovieEdit(UpdateView):
    template_name = "movieedit.html"
    model = Movie
    fields = '__all__'

    def get_success_url(self):
        return reverse('detailMovie', kwargs={'pk': self.object.pk})

class BookEdit(UpdateView):
    template_name = "bookedit.html"
    model = Book
    ffields = '__all__'

    def get_success_url(self):
        return reverse('detailBook', kwargs={'pk': self.object.pk})

class BroadwayEdit(UpdateView):
    template_name = "broadwayedit.html"
    model = Play
    fields = '__all__'

    def get_success_url(self):
        return reverse('detailBroadway', kwargs={'pk': self.object.pk})

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