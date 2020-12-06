from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'

def post_list(request,tag_slug=None): #will get all posts that have the 'published' status
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 5) # 5 posts will be showed in each page
    page = request.GET.get('page') # get current page number
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/post/list.html', {'page':page,'posts':posts,'tag':tag}) #and return the posts in the html page

#Showing a single post
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,publish__month=month,publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:5] #get posts with same tag, retriving the last 5 posts 
    return render(request,'blog/post/detail.html',{'post':post,
                                                   'comments':comments, 
                                                   'new_comment': new_comment, 
                                                   'comment_form':comment_form,
                                                   'similar_posts':similar_posts})

class AddPostView(CreateView):
    model = Post
    template_name = 'blog/post/add_post.html'
    fields = ('author','status','title','slug','body','publish','tags')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)