from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField



class UserModel(models.Model):
    user_field = models.CharField(max_length=255)
    user_data = JSONField()

    def __str__(self):
        return self.user_field
