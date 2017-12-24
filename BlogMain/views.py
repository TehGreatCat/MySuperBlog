from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.


def Mainpage(request):
    posts = Post.objects.all().order_by("timestamp")
    query = request.GET.get('q')
    if query:
        try:
            posts = posts.filter(Q(title__contains=str(query)) | Q(text__contains=str(query))).distinct()
        except Exception as e:
            print(e)
    context = {"posts": posts}
    return render(request, "index.html", context)


def Postpage(request, **kwargs):
    id = kwargs.pop('post_id')
    post = get_object_or_404(Post, post_id=id)
    return render(request, "post.html", {"post": post})


def About(request):
    return render(request, "about.html")


def Pictures(request):
    posts = Post.objects.all().order_by("timestamp")
    context = {"posts": posts}
    return render(request, "pictures.html", context)


def Contacts(request):
    return render(request, "contacts.html")
