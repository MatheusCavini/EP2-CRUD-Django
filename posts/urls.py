from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
     path('', views.PostListView.as_view(), name='index'),
     path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
     path('create/', views.PostCreateView.as_view(), name='create'),
     path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete'),
     path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
     path('<int:post_id>/comment/', views.create_comment, name='comment'),
     path('categories/', views.CategoryListView.as_view(), name='categories'),
     path('categoryFilter/<int:pk>', views.CategoryFilterView.as_view(), name='categoryFilter')
]