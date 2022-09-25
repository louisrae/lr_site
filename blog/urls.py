from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    re_path(r"^$", views.PostList.as_view(), name="index"),
]
