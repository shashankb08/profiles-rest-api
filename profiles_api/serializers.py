from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes  user profile oject"""

    class Meta:
        model = models.UserProfile
        fields = '__all__'

    def create(self, validated_data):
        """ Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updting user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
