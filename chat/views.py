from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import ConnectedUsers
from SimpleChat.cls.state import State

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
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_online(request):
    """API для отримання списку підключених користувачів."""
    users = ConnectedUsers.objects.values_list('first_name', flat=True)
    return Response({'online_users': list(users)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def websocket_connections(request):
    """API для отримання часу підключень через WebSocket (для моніторингу)."""
    return Response({'connection_times': State().get_times()})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def webhook(request):
    """Простий webhook, наприклад, для надсилання повідомлення в кімнату."""
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync

    room = request.data.get("room")
    message = request.data.get("message")

    if not room or not message:
        return Response({"error": "room and message are required"}, status=400)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'chat_{room}',
        {
            'type': 'chat_message',
            'message': message
        }
    )
    return Response({"status": "message sent"})