from django.urls import path
from .views import PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView

urlpatterns = [
    path('posts/',PostListView.as_view()),
    path('post/<str:pk>',PostDetailView.as_view()),
    path('post/delete<str:pk>',PostDeleteView.as_view()),
    path('post/create',PostCreateView.as_view()),
    path('post/update',PostUpdateView.as_view()),
]