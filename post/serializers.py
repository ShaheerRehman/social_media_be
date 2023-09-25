from rest_framework import serializers

from custom_user.serializers import CustomUserSerializer
from like.models import Like
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField()
    apartment = serializers.ReadOnlyField()
    apartment_number = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = '__all__'
        extra_fields = ['is_liked']

    def get_total_likes(self, obj):
        return obj.like_count

    def get_total_comments(self, obj):
        return obj.comment_count

    def get_is_liked(self, obj):
        return Like.objects.filter(user=self.context['request'].user, post=obj.id).exists()

    def get_author(self, obj):
        return obj.author

    def get_apartment(self, obj):
        return obj.apartment

    def get_apartment_number(self, obj):
        return obj.apartment_number
