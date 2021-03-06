from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #creating all fields related to a blog post, that will can be used to filter blog content
    STATUS_CHOICES = (('draft','Draft'),('published','Published'),)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=250, unique_for_date = 'publish') #can be used as tags, in this case, our microorganism
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices=STATUS_CHOICES, default='draft')

    class Meta: #to sort results by publishing field
        ordering = ('-publish',) # - indicates a descending order, so posts published recently will be showed first

    def __str__(self): #human readable string (in this case, title)
        return self.title