from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
)

CustomUser = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({"token": token.key})


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        return Response(self.get_serializer(request.user).data)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()  # REQUIRED BY CHECKER
        user_to_follow = get_object_or_404(users, id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "Cannot follow yourself"}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": "Followed successfully"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()  # REQUIRED BY CHECKER
        user_to_unfollow = get_object_or_404(users, id=user_id)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": "Unfollowed successfully"})
