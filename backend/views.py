from django.shortcuts import render, redirect
from django.db.models import QuerySet
from blog.models import Post
from marketplace.models import Item
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages  # Add this line to import the messages module
import logging
from .forms import UserRegisterForm

logger = logging.getLogger(__name__)

def landing_page(request):
    blog_posts = Post.objects.filter(id__isnull=False).order_by('-publish_date')[:5]
    marketplace_items = Item.objects.all()[:5]
    
    return render(request, 'landing_page.html', {
        'blog_posts': blog_posts,
        'marketplace_items': marketplace_items,
    })
    return render(request, 'landing_page.html')

def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('accounts:login')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logger.info("Logout view accessed")
    logout(request)
    return redirect('accounts:logout')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('blog:index')
         
