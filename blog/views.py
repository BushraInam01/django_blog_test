from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Blog


class BlogListView(View):

    def get(self, request):

        search = request.GET.get("search")
        sort = request.GET.get("sort")

        blogs = Blog.objects.filter(is_active=True)

        if search:
            blogs = blogs.filter(title__icontains=search)

        if sort == "newest":
            blogs = blogs.order_by("-created_at")

        elif sort == "oldest":
            blogs = blogs.order_by("created_at")

        return render(request, "blog/blog_list.html", {"blogs": blogs})


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    pk_url_kwarg = "id"