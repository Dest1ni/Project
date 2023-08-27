from django.urls import path
from .views import ShowPosts,CreatePost,DetailPost
app_name = "posts"

urlpatterns = [
    path('',ShowPosts.as_view(),name="show-posts"),
    path('create/',CreatePost.as_view(),name = "create-post"),
    path('detail/<int:pk>/',DetailPost.as_view(),name = "detail-post")
]