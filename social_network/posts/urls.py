from django.urls import path

from .api import views

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='lists_posts'),
    path('<int:pk>/like/', views.PostLikeView.as_view(), name='like_post'),
    path('', views.PostCreateView.as_view(), name='create_post'),
]
