from django.db import models
from django.db.models import Count

from comment.models import Comment
from custom_user.models import CustomUser
from like.models import Like


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.like_count

    def total_comments(self):
        return self.comment_count

    @property
    def like_count(self):
        return self.likes.aggregate(like_count=Count('id'))['like_count']

    @property
    def comment_count(self):
        return self.comments.aggregate(comment_count=Count('id'))['comment_count']

    @property
    def likes(self):
        return Like.objects.filter(post=self)

    @property
    def comments(self):
        return Comment.objects.filter(post=self)
    #
    # @property
    # def is_liked(self):
    #     return Like.objects.filter(user=self.user, post=self.id).exists()

    @property
    def author(self):
        return self.user.username


    @property
    def apartment(self):
        location = self.user.building_name + ": Apartment " + str(self.user.apartment_number)
        return location

    @property
    def apartment_number(self):
        return self.user.apartment_number