import uuid
from django.db import models


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=50, allow_unicode=True)
    is_private = models.BooleanField()
