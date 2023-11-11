from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
     path('', views.list_posts, name='index'),
     path('<int:post_id>/', views.detail_post, name='detail'),
     path('create/', views.create_post, name='create'),
]