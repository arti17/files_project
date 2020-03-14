from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView


class HomeView(TemplateView):
    template_name = 'home.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
