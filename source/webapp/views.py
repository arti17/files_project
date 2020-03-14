from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

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
        if self.request.user.username:
            form.instance.author = self.request.user
        return super().form_valid(form)


class FileUpdateView(UpdateView):
    model = File
    fields = ['name', 'file', ]
    template_name = 'file_edit.html'


class FileDeleteView(DeleteView):
    model = File
    template_name = 'file_delete.html'
    success_url = reverse_lazy('home')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
