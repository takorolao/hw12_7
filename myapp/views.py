from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})