from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tweet, name='all_tweet'),
    path('add/', views.add_tweet, name='add_tweet'),
    path('<int:id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:id>/delete/', views.delete_tweet, name='delete_tweet'),
    path('search/', views.search_tweet, name='search_tweet'),
    path('<int:tweet_id>/view/', views.view_tweet, name='view_tweet'),
    path('comment/', views.add_comment, name='add_comment'),
]
