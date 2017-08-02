# file for some functions that don't need to live in
# in the django specific files
import os
from django.conf import settings
from django.utils.timezone import localtime, now
from .models import Blog

def get_md_file(md_path):
    md_file = "";
    dir = os.path.join(settings.BASE_DIR, "content/" + md_path) 

    # verifying that the path was made correctly
    print(dir)

    with open(dir) as f:
        md_file = f.read()

    return md_file

def update(blog_name, is_proj):
    file = get_md_file(blog_name + ".md")
    # i can use filter().exists
    if Blog.objects.filter(title=blog_name).exists():
        obj = Blog.objects.get(title=blog_name)
        obj.content = file
        obj.save()
        print("Updating query")
    else:
        obj = Blog()
        obj.title = blog_name
        obj.content = file
        obj.pub_date = now()
        print("Entry does not exist. Creating new entry")

    obj.content = file
    obj.save()
