from django.db import models

# Create your models here.

class Message(models.Model):
    text=models.CharField(max_length=200)
    
    
    """
    The `Message` model represents a message in the database.

    It has one field:
    * `text`: a `CharField` with `max_length` set to `200`
    """

    # the `text` field is a `CharField` with `max_length` set to `200`
    def __str__(self):
        return self.text
        