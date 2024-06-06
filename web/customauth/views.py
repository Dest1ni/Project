from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .models import UserModel
from posts.models import Post
from .forms import UserCreationForm
from django.db.models import Sum

class UserCreationView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'templates/customauth/registration/registration.html'
    success_url = reverse_lazy("posts:show-posts")

class LoginView(BaseLoginView):
    next_page = reverse_lazy("posts:show-posts")
    template_name = 'templates/customauth/registration/login.html'

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy("posts:show-posts")

class ProfileView(DetailView):
    model = UserModel
    context_object_name = "user"
    template_name='templates/customauth/user_templates/profile.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user_id = user.pk ).order_by('-pk').all()
        pos_rep = context['posts'].aggregate(Sum('who_liked'))
        neg_rep = context['posts'].aggregate(Sum('who_disliked'))
        if pos_rep['who_liked__sum'] and neg_rep['who_disliked__sum']:
            context['reputation'] = pos_rep['who_liked__sum'] - neg_rep['who_disliked__sum']
        elif pos_rep['who_liked__sum']:
            context['reputation'] = pos_rep['who_liked__sum']
        elif neg_rep['who_disliked__sum']:
            context['reputation'] = - neg_rep['who_disliked__sum']
        else:
            context['reputation'] = 0
        return context
