from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Like, Comment
from .forms import CommentForm


#Blog view
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


#Blog Details view
class BlogDetailView(View):

    def get(self, request, id):

        blog = get_object_or_404(Blog, id=id)

        likes_count = Like.objects.filter(
            blog=blog
        ).count()

        if request.user.is_authenticated:

            user_has_liked = Like.objects.filter(
                blog=blog,
                user=request.user
            ).exists()

        else:

            user_has_liked = False

        comments = Comment.objects.filter(
            blog=blog
        ).order_by("-created_at")

        comment_form = CommentForm()

        context = {
            "blog": blog,
            "likes_count": likes_count,
            "user_has_liked": user_has_liked,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(
            request,
            "blog/blog_detail.html",
            context
        )


#Like view
class LikeView(LoginRequiredMixin, View):

    def post(self, request, id):

        blog = get_object_or_404(Blog, id=id)

        like, created = Like.objects.get_or_create(
            user=request.user,
            blog=blog
        )

        if not created:
            like.delete()

        return redirect("blog_detail", id=id)


#Comment view
class CommentView(LoginRequiredMixin, View):

    def post(self, request, id):

        blog = get_object_or_404(Blog, id=id)

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.user = request.user
            comment.blog = blog

            comment.save()

        return redirect("blog_detail", id=id)