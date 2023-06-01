from django.contrib import admin
from .models import TodoItem, Tag

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
