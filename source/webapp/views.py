from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, CreateView

from webapp.models import File


class HomeView(ListView):
    template_name = 'home.html'
    model = File
    ordering = '-created_at'


class FileDetailView(DetailView):
    template_name = 'file_detail.html'
    model = File


class FileCreateView(CreateView):
    template_name = 'file_create.html'
    model = File
    fields = ['name', 'file', ]

    def form_valid(self, form):
        if self.request.user:
            form.instance.author = self.request.user
        return super().form_valid(form)


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
