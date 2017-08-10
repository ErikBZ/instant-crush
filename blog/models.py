from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Quotes(models.Model):
    author_first = models.CharField(max_length=50)
    author_last = models.CharField(max_length=50)
    quote = models.TextField()

    # to string
    def __unicode__(self):
        return self.author_last + ", " + author_first
    
    def __str__(self):
        return self.author_last + ", " + author_first
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # a bunch of text 
    content = models.TextField()
    is_project = models.BooleanField(default=False)

    # to string
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("blog_detail", kwargs={"id": self.id})

    def get_summary(self):
        chars = self.content[0:200]
        sum = ""

        for i in range(len(chars)-1, -1 ,-1):
            if chars[i] == ' ':
                sum = chars[0:i]
        
        return chars
