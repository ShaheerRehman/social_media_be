from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    author = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author(self, obj):
        return obj.author