from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('', views.Home.as_view(), name="books"), 
    path('', views.Home.as_view(), name="movies"), 
    path('', views.Home.as_view(), name="broadways"), 

    path('movies/', views.Movies.as_view(), name="movies"),
    path('movies/new/', views.AddMovie.as_view(), name='addmovie'), 
    path('movies/<int:pk>', views.DetailMoviePage.as_view(), name="detailMovie"),
    path('addmovie/', views.AddMovie.as_view(), name="addmovie"),
    path('moive/<int:pk>/delete', views.MovieDelete.as_view(), name="moviedelete"),
    path('moive/<int:pk>/edit', views.MovieEdit.as_view(), name="movieedit"),
    
    path('books/', views.Books.as_view(), name="books"),
    path('books/new/', views.AddBook.as_view(), name='addbook'),
    path('books/<int:pk>', views.DetailBookPage.as_view(), name="detailBook"),
    path('addbook/', views.AddBook.as_view(), name="addbook"),
    path('book/<int:pk>/delete', views.BookDelete.as_view(), name="bookdelete"),
    path('book/<int:pk>/edit', views.BookEdit.as_view(), name="bookedit"),

    path('broadways/', views.Broadways.as_view(), name="broadways"),
    path('broadways/new/', views.AddPlay.as_view(), name='addplay'),
    path('broadways/<int:pk>', views.DetailBroadwayPage.as_view(), name="detailBroadway"),
    path('addplay/', views.AddPlay.as_view(), name="addplay"),
    path('broadway/<int:pk>/delete', views.BroadwayDelete.as_view(), name="broadwaydelete"),
    path('broadway/<int:pk>/edit', views.BroadwayEdit.as_view(), name="broadwayedit"),

    path('user/<username>', views.Lists.as_view(), name='lists'),
    path('lists/new/', views.CreateList.as_view(), name='createList'),
    path('lists/<int:pk>', views.DetailList.as_view(), name="detailList"),
    path('lists/<int:pk>/update', views.UpdateList.as_view(), name='listUpdate'),
    path('lists/<int:pk>/delete', views.DeleteList.as_view(), name='listDelete'),

    path('user/<username>', views.Profile, name="profile"),
    path('accounts/signup/', views.Signup, name='signup'),
]