from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from social import models

class Wall(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'social/wall.html'
    login_url = 'auth/login'

    def get_queryset(self):
        self.request.user
        return models.Post.objects.filter(User__person1 = self.request.user.id)
