from django.views.generic import TemplateView
from customauth.models import UserModel

class IndexView(TemplateView):
    template_name='web/index.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = UserModel
        if self.request.user.is_authenticated:
            context["message"] = f"Welcome to the web {user.username}"
        else:
            context["message"] = f"Welcome to the web Anonymous"
        return context