from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    subtitle = models.TextField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=200, default=title)

    def __str__(self) -> str:
        return self.title
