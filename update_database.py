import os
import blog.models
from blog.helper import update

def create_obj(name, file_content, is_proj):
    obj = Blog()
    # create file with name
    obj.title = name;
    # and save the contets
    obj.content = file_content
    obj.pub_date = now()
    obj.is_project = is_proj
    obj.save()

def update_obj(obj, new_content):
    obj.content = new_content
    obj.save()

# chdir into either project or blogs
# project is true if the dir is the proj dir
def check_files(project):
    files = os.listdir(os.curdir)
    for f in files:
        if os.listdir(f):
            raise Exception("There shouldn't be any folders where the markdown files are stored")

def update():
    abs_pth = os.path.abspath(os.curdir)
    content_path = os.path.join(abs_pth, "content")
    print(content_path)
    os.chdir("projects")
    update(True)
    os.chdir("../blogs")
    update(False)

update()

