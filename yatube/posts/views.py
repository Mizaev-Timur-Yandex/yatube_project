from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Yatube для друзей'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_posts.html'

    return HttpResponse(request,f'Страница группы: {slug}')

def group_list(request):
    template = 'posts/group_list.html'
    title = 'Yatube для друзей'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {

        'title': title,
        'text': text,
    }
    return render(request, template, context)