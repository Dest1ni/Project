from django.urls import path
from .views import ShowPosts,CreatePost,DetailPost,ReactionPostView,CommentCreateView
app_name = "posts"

urlpatterns = [
    path('',ShowPosts.as_view(),name="show-posts"),
    path('create/',CreatePost.as_view(),name = "create-post"),
    path('detail/<int:pk>/',DetailPost.as_view(),name = "detail-post"),
    path('like/<int:post_id>/<str:reaction>',ReactionPostView.as_view(),name= "reaction-post"),
    path('comment/<int:post_id>/',CommentCreateView.as_view(),name="comment-post")
]