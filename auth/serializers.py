from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())], max_length=50)
    password = serializers.CharField(max_length=50, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']