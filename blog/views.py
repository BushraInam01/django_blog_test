from django.shortcuts import render
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    return render(request, "blog/blog_list.html", {"blogs": blogs})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)

    return render(request, "blog/blog_detail.html", {"blog": blog})