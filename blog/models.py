from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager): #creating class to filter only posts that are published
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model): #creating all fields related to a blog post, that will can be used to filter blog content
    STATUS_CHOICES = (('draft','Draft'),('published','Published'),)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=250, unique_for_date='publish') #can be used as tags, in this case, our microorganism
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager() #in this blog, our tags will be microorganisms names

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

    class Meta: #to sort results by publishing field
        ordering = ('-publish',) # - indicates a descending order, so posts published recently will be showed first

    def __str__(self): #human readable string (in this case, title)
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') #associate the comment to a specific post
    nome = models.CharField(max_length = 120)
    email = models.EmailField()
    texto = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.nome} on {self.post}'
