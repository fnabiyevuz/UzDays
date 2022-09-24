from django.urls import path

from article.views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('category/<str:name>/', Category),
    path('region/<str:name>/', Region),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('article/<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleView.as_view()),
    path('search/', Search)
]


