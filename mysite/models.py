from django.db import models
import django.utils.timezone as timezone


class Image(models.Model):
    name = models.CharField(max_length=30)
    like = models.IntegerField(default=0)
    comments = models.TextField(default='')

    def screenshots_as_list(self):
        return self.comments.split('\n')


class WordPost(models.Model):
    word_id = models.IntegerField(default=0)
    message = models.CharField(max_length=151)
    like = models.IntegerField(default=0)
    comments = models.TextField(default='')
    datetime = models.DateTimeField(default=timezone.now)

    def screenshots_as_list(self):
        return self.comments.split('\n')


class Files(models.Model):
    name = models.CharField(max_length=30)
    like = models.IntegerField(default=0)
    comments = models.TextField(default='')

    def screenshots_as_list(self):
        return self.comments.split('\n')
