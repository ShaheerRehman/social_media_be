from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Like
        fields = '__all__'
