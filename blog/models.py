from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.charField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # blog text stored as .md
    # first i need to figure out how to make one
    # blog_text = models.
