from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=144, blank=False)
    content = models.TextField(max_length=4096)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id', 'author')
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        db_table = 'posts'


class Like(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        db_table = 'likes'
