from django.contrib import admin
from reviews.models import Category, Genre, Review, Title
from reviews.models import User, Comment
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Title)
