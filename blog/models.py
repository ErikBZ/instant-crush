from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # a bunch of text 
    blog_text = models.TextField()

    #to string
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
