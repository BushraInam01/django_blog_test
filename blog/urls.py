from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:id>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/<int:id>/like/", views.LikeView.as_view(), name="blog_like"),
    path("blogs/<int:id>/comment/", views.CommentView.as_view(), name="blog_comment"),
]