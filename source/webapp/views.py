from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView

from webapp.models import File


class HomeView(ListView):
    template_name = 'home.html'
    model = File
    ordering = '-created_at'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
