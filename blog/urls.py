from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import AddPostView

app_name = 'blog'

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
]