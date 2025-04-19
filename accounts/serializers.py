from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES)
    birth_date = serializers.DateField()
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'gender', 'birth_date', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        profile = UserProfile.objects.create(
            user=user,
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date']
        )
        return profile

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'gender', 'birth_date']