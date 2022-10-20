from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, permissions

from users.models import UserInfo
from users.serializers import UserInfoSerializer


class UserInfoView(generics.RetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserInfoSerializer

    def get_object(self) -> UserInfo:
        try:
            return UserInfo.objects.get(user=self.request.user)
        except UserInfo.DoesNotExist:
            raise Http404
