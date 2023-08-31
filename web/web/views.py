from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name='web/index.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["message"] = f"Welcome to the web {self.request.user.username}"
        else:
            context["message"] = "Welcome to the web Anonymous"
        return context