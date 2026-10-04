from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
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
class BlogDetailView(DetailView):

    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["likes_count"] = Like.objects.filter(
            blog=self.object
        ).count()

        if self.request.user.is_authenticated:

            context["user_has_liked"] = Like.objects.filter(
                blog=self.object,
                user=self.request.user
            ).exists()

        else:

            context["user_has_liked"] = False

        context["comments"] = Comment.objects.filter(
            blog=self.object
        ).order_by("-created_at")

        context["comment_form"] = CommentForm()

        return context


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