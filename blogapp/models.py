from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Article(models.Model):
    """docstring for Product."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
