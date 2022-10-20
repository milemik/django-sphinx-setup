from rest_framework import serializers

from users.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ("user", "first_name", "last_name", "email", "birth_date")
        read_only_fields = ("user",)
