from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
