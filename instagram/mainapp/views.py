from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    return render(request, 'home.html', { 'posts': posts})

def new(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'new.html',context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()
    context = {
        'form': form
    }

    return 