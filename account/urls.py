from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='manage'),
    path('login/', Login),
    path('logout/', Logout),
]