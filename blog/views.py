from django.shortcuts import render
from django.views import generic

from .models import Post

# Create your views here.


class PostList(generic.ListView):
    posts = Post.objects.order_by("-create_date")
    template_name = "index.html"

    def get_queryset(self):
        return Post.objects.order_by("-create_date")


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
