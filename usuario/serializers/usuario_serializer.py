from usuario.models import User, Post

from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password errado."})

        return attrs

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
        )
        user.set_password(validate_data['password'])
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    formatted_created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'full_name', 'username',
            'image', 'mensagem', 'imagem', 'created_at', 'formatted_created_at']
        read_only_fields = ['user', 'created_at']

    def get_full_name(self, obj):
        return obj.user.profile.full_name if obj.user.profile else ''

    def get_username(self, obj):
        return obj.user.username

    def get_image(self, obj):
        if obj.user.profile and obj.user.profile.image:
            image_url = obj.user.profile.image.url
            return self.context['request'].build_absolute_uri(image_url)
        else:
            return None
    def get_formatted_created_at(self, obj):
        return obj.formatted_created_at()

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post
