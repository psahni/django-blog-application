from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.


def index(request):
    # Get the blog posts that are published
    posts = Post.objects.filter(published=True)
    #Now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})



def post(request, slug):
    # Get the Post object