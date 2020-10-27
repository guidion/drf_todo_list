from django.db.models import Model, CharField, TextField


# Create your models here.
class Tasks(Model):
    """
    Tasks Model
    """
    title = CharField(max_length=255)
    description = TextField()
