from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POSTS_PER_PAGE = 10


def index(request):
    # Определяем шаблон и переменные контекста
    template = 'posts/index.html'

    # Получаем последние 10 опубликованных постов
    posts = Post.objects.order_by('-pub_date')[:POSTS_PER_PAGE]

    # Сохраняем переменные контекста в словаре
    context = {
        'posts': posts,
    }

    # Рендерим шаблон и передаем словарь контекста
    return render(request, template, context)


def group_posts(request, slug):
    # Получаем объект группы по переданному слагу
    group = get_object_or_404(Group, slug=slug)

    # Получаем все посты из этой группы и сортируем их
    # по дате публикации (сначала новые)
    posts = group.Post.order_by('-pub_date')[:POSTS_PER_PAGE]

    template = 'posts/group_list.html'

    # Сохраняем переменные контекста в словаре
    context = {
        'group': group,
        'posts': posts,
    }

    # Рендерим шаблон и передаем словарь контекста
    return render(request, template, context)
