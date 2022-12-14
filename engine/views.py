from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from engine.models import *
from engine.forms import *

def home(request):
    posts = Post.objects.all()
    return render(request, 'engine/home.html', context={'posts': posts})


def create(request):
    initialize()
    postform = PostForm()
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('home')
    else:
        return render(request, 'engine/create.html', {'form': postform})


def edit(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h1>Post is not found</h1>')
    postform = PostForm()
    if request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('home')
    else:
        return render(request, 'engine/edit.html', {'form': postform})


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound('<h1>Post is not found</h1>')


def initialize():
    if Author.objects.all().count() == 0:
        Author.objects.create(name='Автор 1')
        Author.objects.create(name='Автор 2')
        Author.objects.create(name='Автор 3')

    if Publisher.objects.all().count() == 0:
        Publisher.objects.create(name='Издательство 1')
        Publisher.objects.create(name='Издательство 2')
        Publisher.objects.create(name='Издательство 3')

    if Category.objects.all().count() == 0:
        Category.objects.create(name='Категория 1')
        Category.objects.create(name='Категория 2')
        Category.objects.create(name='Категория 3')