from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreationForm
# Create your views here.

class ShowPosts(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        return Post.objects.all()

class DetailPost(DetailView):
    model = Post
    template_name = "posts/detail.html"

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    form_class  = PostCreationForm
    login_url = reverse_lazy("cauth:cauth-login")
    template_name = "posts/create.html"
    success_url = reverse_lazy("posts:show-posts")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    