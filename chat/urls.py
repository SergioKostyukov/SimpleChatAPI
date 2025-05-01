from django.urls import path
from .views import ChatListCreateView, MessageCreateView, MessageListView
from . import views

urlpatterns = [
    path('webhook/', views.webhook),
    path('online/', views.users_online),
    path('chats/', ChatListCreateView.as_view(), name='chats'),
    path('message/send/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:chat_id>/', MessageListView.as_view(), name='message-list'),
]