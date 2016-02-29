# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from django.conf import settings

import json

from .models import Post, PostForm

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):

    error = None
    if request.method == 'POST':
        submitted = PostForm(request.POST)
        if submitted.is_valid():
            submitted.save()
        else:
            error = submitted

    debug = str(request.META)
    posts = Post.objects.all()
    form = PostForm

    cookies = str(request.COOKIES)

    return render_to_response('hello.html', {'debug': debug, 'posts': posts, 'form': form, 'error': error, 'cookies': cookies}, context_instance=RequestContext(request))

def post_echo(request):

    if request.method == 'POST':
        posted = request.POST
    else:
        posted = None

    return render_to_response('post_echo.html', {'posted': posted, 'dir_request': dir(request)}, context_instance=RequestContext(request))


def json_example(request):
    response = { 
          "userId": 1,
          "id": 1,
          "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
          "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
        }

    loaded = json.dumps(response)
    return HttpResponse(loaded, content_type='application/json')

def unicode_401(request):

    response = 'مرحبا يا عالم'
    return HttpResponse(response, status=401)

