from rest_framework import generics
from .models import About
from .serializers import AboutSerializer
from rest_framework.permissions import AllowAny

class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return About.objects.first()