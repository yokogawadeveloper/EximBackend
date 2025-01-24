from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({"data": serializer.data, "message": "Login successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Something is wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "message": "Logout successfully"}, status=status.HTTP_204_NO_CONTENT)
