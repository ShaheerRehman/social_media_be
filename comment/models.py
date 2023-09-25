from django.db import models


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    @property
    def author(self):
        return self.user.username
