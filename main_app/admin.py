from django.contrib import admin
from .models import Book
from .models import Movie
from .models import Play
from .models import List

admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Play)
admin.site.register(List)

