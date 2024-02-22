from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,View
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreationForm,CommentCreationForm

class ShowPosts(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by("-id").all()

class DetailPost(DetailView):
    model = Post
    template_name = "posts/detail.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        post:Post = self.get_object()

        comments:Comment = Comment.objects.filter(post_id = post.pk)

        context['likes'] = post.who_liked.count()
        context['dislikes'] = post.who_disliked.count()
        context['comment_form'] = CommentCreationForm() 
        context['comments'] = comments
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

    def post(self, request,*args, **kwargs):
        post_id = request.POST.get('post_id')
        reaction = request.POST.get('reaction')
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

        elif reaction=='dislike':
            if post.who_disliked.filter(id=user.id).exists():
                post.who_disliked.remove(user)
            elif post.who_liked.filter(id=user.id).exists():
                post.who_liked.remove(user)
                post.who_disliked.add(user)
            else:
                post.who_disliked.add(user)

        dislikes = post.who_disliked.count()
        likes = post.who_liked.count()
        
        return JsonResponse({'post_id':post_id,'dislikes':dislikes,'likes':likes})
    
    def get(self, request, post_id,reaction, *args, **kwargs):
        return HttpResponseRedirect(reverse('posts:detail-post', args=[post_id]))
    
        
class ReactionCommentView(LoginRequiredMixin,View):
    login_url = reverse_lazy("cauth:cauth-login")
    
    def post(self,request,*args,**kwargs):
        comment_id = request.POST.get("comment_id")
        user = request.user
        comment = get_object_or_404(Comment,id = comment_id)
        if comment.likes.filter(id = user.id).exists():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        likes = comment.likes.count()
        return JsonResponse({'likes':likes})
    
class CommentCreateView(LoginRequiredMixin,View):
    login_url = reverse_lazy("cauth:cauth-login")

    def post(self,request,post_id):
        post = get_object_or_404(Post,id = post_id)

        user = request.user

        body = request.POST.get('body')

        comment = Comment.objects.create(
            body = body,
            post = post,
            user = user,
        )

        return HttpResponseRedirect(reverse('posts:detail-post', args=[post_id]))
    
    def get(self,request,post_id):
        return HttpResponseRedirect(reverse('posts:detail-post', args=[post_id]))

