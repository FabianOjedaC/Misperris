from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Sistema.quickstart.serializers import UserSerializer, GroupSerializer

class UserSerializer(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class GroupSerializer(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)
