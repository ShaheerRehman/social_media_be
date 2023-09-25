from django.db import models


class Like(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.post.title
