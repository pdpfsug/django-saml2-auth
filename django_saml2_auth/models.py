from django.db import models

class IdentityProvider(models.Model):
    """
    Module to incapsulate information from IdP

    """

    entity_id = models.CharField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    url_metadata = models.URLField(primary_key=True)
    cert = models.TextField()
    attributes_map = models.TextField(
            help_text="JSON object to map IdP returned attributes to user model fields")  # Text for portability
    is_enabled = models.BooleanField(
            default=True,
            help_text="Enable or disable this IdP")

    def __unicode__(self):
        return u"{name} {entity_id}"
