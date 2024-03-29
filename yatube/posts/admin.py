# импорты из стандартной библиотеки
from django.contrib import admin

# импорты модулей текущего проекта
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Определяет отображение полей модели Post в админке."""
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
