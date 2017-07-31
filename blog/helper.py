# file for some functions that don't need to live in
# in the django specific files
import os
from django.conf import settings

def get_md_file(md_path):
    md_file = "";
    dir = os.path.join(settings.BASE_DIR, "content/" + md_path) 

    # verifying that the path was made correctly
    print(dir)

    with open(dir) as f:
        md_file = f.read()

    return md_file
