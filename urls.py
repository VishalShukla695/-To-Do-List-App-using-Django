from django.urls import path
from todo_list_app.views import TodoItemListCreateAPIView, TodoItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/todo/', TodoItemListCreateAPIView.as_view(), name='todo-list-create'),
    path('api/todo/<int:pk>/', TodoItemRetrieveUpdateDestroyAPIView.as_view(), name='todo-item-detail'),
]
