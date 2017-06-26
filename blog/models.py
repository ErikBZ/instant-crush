from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # a bunch of text 
    content = models.TextField()

    #to string
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("blog_detail", kwargs={"id": self.id})
