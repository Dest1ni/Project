from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .models import UserModel
from posts.models import Post
from .forms import UserCreationForm


class UserCreationView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy("posts:show-posts")

class LoginView(BaseLoginView):
    next_page = reverse_lazy("main-page")
    template_name = 'registration/login.html'

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy("main-page")

class ProfileView(DetailView):
    model = UserModel
    context_object_name = "user"
    template_name='user_templates/profile.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user: UserModel = self.get_object()
        context['posts'] = Post.objects.filter(user_id = user.pk ).order_by('-pk').all()
        return context
