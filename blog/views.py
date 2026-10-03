from django.shortcuts import render
from django.views import View
from .models import Blog


class BlogListView(View):

    def get(self, request):

        search = request.GET.get("search")
        sort = request.GET.get("sort")

        blogs = Blog.objects.all()

        if search:
            blogs = blogs.filter(
                title__icontains=search
            )

        if sort == "newest":
            blogs = blogs.order_by("-created_at")

        elif sort == "oldest":
            blogs = blogs.order_by("created_at")

        return render(
            request,
            "blog/blog_list.html",
            {"blogs": blogs}
        )


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)

    return render(
        request,
        "blog/blog_detail.html",
        {"blog": blog}
    )