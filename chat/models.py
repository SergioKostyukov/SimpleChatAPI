from django.db import models
from accounts.models import UserProfile

class Chat(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(UserProfile, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.created_at}"
    
class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s connected at %s" % (self.first_name, self.connected)