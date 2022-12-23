from rest_framework import serializers
from api.models import Repos


class ReposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repos
        fields = [
            'id',
            'name',
        ]
