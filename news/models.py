from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def short_content(self):
        short = self.content[:300]
        if len(self.content) > 300:
            short += '...'
        return short

    def __str__(self):
        return f'{self.id}, {self.title}, {self.pub_date}'

