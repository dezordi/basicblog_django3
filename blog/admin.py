from django.contrib import admin
from .models import Post


@admin.register(Post) #registering the class Post created on models.py
class PostAdmin(admin.ModelAdmin): #configuring the structure of post information on admin section of blog
    #the three first variables creates basic menus on django admin blog site to filter and view posts
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)} #create automatically the slug with the title in lowercase letters with hiphen as space
    raw_id_fields = ('author',) #creates a model of searching authors by ID number
    date_hierarchy = 'publish'
    ordering = ('status','publish')