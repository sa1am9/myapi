from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from account.models import Account



class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'password']

    def validate(self, data):
        username = data['username']
        user_qs = Account.objects.filter(username=username)
        if user_qs.exists():
            raise ValueError("This user has already registered.")
        return data

    def save(self):

        account = Account(username=self.validated_data['username'])
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account

class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk',  'username', ]



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Account
        fields = ['username', 'password']

    def validate(self, data):

        username = data['username']
        password = data['password']
        user = Account.objects.filter(username=username)
        if not user.exists():
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        user = user.first()
        if not user.check_password(password):
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except Account.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }