from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:id>/", views.blog_detail, name="blog_detail"),
]