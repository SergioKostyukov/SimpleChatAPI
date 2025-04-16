from django.urls import path
from .views import ChatListCreateView, MessageCreateView, MessageListView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chats'),
    path('message/send/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:chat_id>/', MessageListView.as_view(), name='message-list'),
]