import uuid
from django.db import models


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=50, allow_unicode=True)
    is_private = models.BooleanField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Local(models.Model):
    local_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    address = models.TextField()
    opening_hours = models.TextField()
    image_url = models.URLField()
    open = models.BooleanField()
