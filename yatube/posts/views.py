from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    # Определяем шаблон и переменные контекста
    template = 'posts/index.html'
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'

    # Получаем последние 10 опубликованных постов
    posts = Post.objects.order_by('-pub_date')[:10]

    # Сохраняем переменные контекста в словаре
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }

    # Рендерим шаблон и передаем словарь контекста
    return render(request, template, context)


def group_posts(request, slug):
    # Получаем объект группы по переданному слагу
    group = get_object_or_404(Group, slug=slug)

    # Получаем все посты из этой группы и сортируем их
    # по дате публикации (сначала новые)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    # Формируем заголовок страницы
    title = f'Группа {slug}'
    template = 'posts/group_list.html'

    # Сохраняем переменные контекста в словаре
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }

    # Рендерим шаблон и передаем словарь контекста
    return render(request, template, context)
