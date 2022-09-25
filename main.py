import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lr_site.settings")
django.setup()


from blog.models import Post


def create_post(title, content, author, slug):

    p = Post(title=title, content=content, author=author, slug=slug)
    p.save()


create_post()
