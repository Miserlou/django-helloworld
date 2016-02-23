from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length='200')
    body = models.TextField()    
    date = models.DateTimeField('date', blank=True, default=datetime.now)

    def __unicode__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('date',)