from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

# Клас для перегляду списку чатів та створення нового чату
class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

# Клас для створення нового повідомлення
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

# Перегляд усіх повідомлень для чату
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat__id=chat_id)