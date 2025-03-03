from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Automatically gets CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']  # Include 'username' if required
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create user and ensure a default username if missing"""
        username = validated_data.get("username", None)
        
        if not username:  # If no username is provided, use email as username
            validated_data["username"] = validated_data["email"].split('@')[0]
        
        user = User.objects.create_user(**validated_data)
        return user
