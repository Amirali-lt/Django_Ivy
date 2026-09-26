from django.db import models
import uuid

class Project (models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False,blank=False,max_length=200)
    def __str__(self):
        return self.title
