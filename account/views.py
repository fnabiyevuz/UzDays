from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import *


class HomeView(LoginRequiredMixin, CreateView):
    login_url = '/manage/login/'
    template_name = "manage-home.html"
    model = Article
    fields = ['category', 'region', 'title', 'photo', 'text', 'user']

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/manage/')
        else:
            messages.error(request, 'Login yoki Parol notogri kiritildi!')
            return redirect('/manage/login/')
    else:
        return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Tizimdan chiqish muvaffaqiyatli yakunlandi!")
    return redirect('/manage/login/')