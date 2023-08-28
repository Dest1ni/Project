from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreationForm

class ShowPosts(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()

class DetailPost(DetailView):
    model = Post
    template_name = "posts/detail.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post:Post = self.get_object()
        context['likes'] = post.who_liked.count()
        context['dislikes'] = post.who_disliked.count()
        return context

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    form_class  = PostCreationForm
    login_url = reverse_lazy("cauth:cauth-login")
    template_name = "posts/create.html"
    success_url = reverse_lazy("posts:show-posts")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ReactionPostView(LoginRequiredMixin,View):
    login_url = reverse_lazy("cauth:cauth-login")
    def post(self, request, post_id,reaction, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)

        user = request.user
        if reaction=='like':
            if post.who_liked.filter(id=user.id).exists():
                post.who_liked.remove(user)
            elif post.who_disliked.filter(id=user.id).exists():
                post.who_disliked.remove(user)
                post.who_liked.add(user)
            else:
                post.who_liked.add(user)
        if reaction=='dislike':
            if post.who_disliked.filter(id=user.id).exists():
                post.who_disliked.remove(user)
            elif post.who_liked.filter(id=user.id).exists():
                post.who_liked.remove(user)
                post.who_disliked.add(user)
            else:
                post.who_disliked.add(user)
        return HttpResponseRedirect(reverse('posts:detail-post', args=[post_id]))
    def get(self,request,post_id,*args,**kwargs):
        return HttpResponseRedirect(reverse('posts:detail-post', args=[post_id]))
    

