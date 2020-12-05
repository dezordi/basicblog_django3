from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request): #will get all posts that have the 'published' status
    post = Post.published.all()
    return render(request,'blog/post/list.html', {'posts':post}) #and return the posts in the html page

#Showing a single post
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post/detail.html',{'post':post})