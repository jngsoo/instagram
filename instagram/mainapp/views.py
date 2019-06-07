from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse

try:
    from django.utils import simplejson as json
except ImportError:
    import json

# Create your views here.

def home(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    return render(request, 'home.html', { 'posts': posts})

def about(request):
    return render(request, 'about.html')

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

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    return redirect('home')

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user # 로그인한 유저를 가져온다.
        post_id = request.POST.get('pk', None)
        post = Post.objects.get(pk = post_id) #해당 메모 오브젝트를 가져온다.

        if post.likes.filter(id = user.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            post.likes.remove(user) #likes 컬럼에서 해당 유저를 지운다.
            message = 'You disliked this'
        else:
            post.likes.add(user)
            message = 'You liked this'

    context = {'likes_count' : post.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')
    # dic 형식을 json 형식으로 바꾸어 전달한다.