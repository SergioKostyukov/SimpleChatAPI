from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from .models import UserProfile
from .serializers import UserRegistrationSerializer, UserProfileSerializer

# Реєстрація користувача
class RegisterUserView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# Вхід до системи
class LoginUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=user_obj.username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            
            # Отримати профіль користувача
            try:
                profile = UserProfile.objects.get(user=user)
                profile_id = profile.id
            except UserProfile.DoesNotExist:
                profile_id = None

            return Response({
                'token': token.key,
                'user_id': profile_id
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# Профіль користувача
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get('pk')  # або 'id' – залежно від url pattern
        return UserProfile.objects.get(pk=user_id)
