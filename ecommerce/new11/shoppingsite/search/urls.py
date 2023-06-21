from shop import views
from django.urls import path
from search.views import *
from search import views

app_name = 'search'
urlpatterns = [
    path('search/',views.searchresult,name="searchresult"),
    ]