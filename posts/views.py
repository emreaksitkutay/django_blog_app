from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def posts_view(request):
    deleted_posts = Post.objects.filter(user=request.user, is_deleted=True)
    user_posts = Post.objects.filter(user=request.user, is_deleted=False)
    return render(request, 'posts.html', {'posts': user_posts, 'deleted_posts': deleted_posts})

def base(request):
    return render(request, 'base.html')

def create_post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user

        post = Post(title=title, description=description, image=image, user=user)
        post.save()
        return redirect('posts')

    return render(request, 'create_post.html')

def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.is_deleted = True
        post.save()
        return redirect('posts')
    
    return render(request, 'delete_post.html', {'post': post})

def republish_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.is_deleted = False
        post.save()
        return redirect('posts')
    
    return render(request, 'republish_post.html', {'post': post})


def edit_post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'edit_post.html', {'post': post})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('base.html')


def mainpage_view(request):
    posts = Post.objects.all()
    return render(request, 'mainpage.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profiles/profile.html', {'user': user})