from django.urls import path

from . import views

app_name = "app_articles"

urlpatterns = [
    path('', views.view_articles, name = 'link_articles'),
    path('creer/', views.view_creer, name = 'link_creer'),
    path('<slug:slug>/', views.view_article, name = 'link_article'),
]