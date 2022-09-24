import datetime
from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import *


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = 'active'
        category = Categories.objects.all()
        context['categories'] = category
        context['category_first'] = Categories.objects.first()
        context['regions'] = Regions.objects.all()
        dateminus7 = datetime.now() - timedelta(days=7)
        articles = Article.objects.filter(date__gte=dateminus7)
        if len(articles) < 20:
            articles = Article.objects.all()
        context['article3'] = articles.order_by('-id')[0:3]
        context['article4'] = articles.order_by('-id')[3:4].first()
        paginator = Paginator(articles.order_by('-id')[4:19], 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['article15'] = page_obj
        context['views5'] = articles.order_by('-views')[0:5]
        context['views10'] = articles.order_by('-views')[5:14]
        ads = Advertisement.objects.all()
        context['ads'] = ads
        # context['ads1'] = ads[0:1].first()
        # context['ads2'] = ads[1:2].first()
        # print(ads[0:1].first().photo.url)

        return context


def Category(request, name):
    dateminus7 = datetime.now() - timedelta(days=7)
    articles = Article.objects.filter(date__gte=dateminus7)
    article = articles.filter(category__name=name).order_by('-id')
    views = articles.order_by('-views')[0:15]
    paginator = Paginator(article, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': name,
        'categories': Categories.objects.all(),
        'regions': Regions.objects.all(),
        'articles': page_obj,
        'views': views
    }
    return render(request, 'category.html', context)


def Region(request, name):
    dateminus7 = datetime.now() - timedelta(days=7)
    articles = Article.objects.filter(date__gte=dateminus7)
    article = articles.filter(region__name=name).order_by('-id')
    views = articles.order_by('-views')[0:15]
    paginator = Paginator(article, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'region': name,
        'categories': Categories.objects.all(),
        'regions': Regions.objects.all(),
        'articles': page_obj,
        'views': views
    }
    return render(request, 'region.html', context)


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = 'active'
        context['categories'] = Categories.objects.all()
        context['regions'] = Regions.objects.all()
        context['aboutus'] = AboutUs.objects.first()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = 'active'
        context['categories'] = Categories.objects.all()
        context['regions'] = Regions.objects.all()
        return context


class ArticleView(DetailView):
    model = Article
    template_name = "article.html"
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['regions'] = Regions.objects.all()
        context['top_articles'] = Article.objects.order_by('-views')[0:15]
        context['previous'] = Article.objects.filter(category=self.object.category, id__gt=self.object.id).order_by(
            '-id').first()
        context['next'] = Article.objects.filter(category=self.object.category, id__lt=self.object.id).first()
        ip = self.request.get_host().split(':')
        print(ip[0], self.object.ips)
        if self.object.ips is not None:
            if ip[0] in self.object.ips:
                pass
            else:
                self.object.ips += ip[0] + ' '
                self.object.views_count()
        else:
            self.object.ips = ip[0] + ' '
            self.object.views_count()
        return context


def Search(request):
    name = request.GET['search']
    dateminus7 = datetime.now() - timedelta(days=7)
    articles = Article.objects.filter(date__gte=dateminus7)
    article = Article.objects.filter(title__contains=name)
    views = articles.order_by('-views')[0:15]
    paginator = Paginator(article, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(article) == 0:
        count = 0
    else:
        count = 1
    context = {
        'region': name,
        'categories': Categories.objects.all(),
        'regions': Regions.objects.all(),
        'articles': page_obj,
        'views': views,
        'count': count
    }
    return render(request, 'search.html', context)


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
