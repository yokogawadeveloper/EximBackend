from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User


# Create serializers here.
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    default_error_messages = {"username": "The username should only contain alphanumeric characters"}

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")

        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3, write_only=True)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "password", "tokens"]

    def get_tokens(self, obj):
        user = User.objects.get(username=obj["username"])
        return {"refresh": user.tokens()["refresh"], "access": user.tokens()["access"]}

    def validate(self, attrs):
        user = User.objects.get(username=attrs["username"])
        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError("Invalid password please tyr again")

        if user is None:
            raise serializers.ValidationError("Invalid username or password")

        if not user.is_verified:
            raise serializers.ValidationError("Please verify your email")
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {"bad_token": "Token is expired or invalid"}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        depth = 1

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
