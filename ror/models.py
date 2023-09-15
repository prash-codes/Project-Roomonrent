from django.db import models

# Create your models here.

class Room(models.Model):
    room_image = models.ImageField(upload_to="static/images")
    room_address = models.CharField(max_length=512)
    owner = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    room_rent = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.owner} {self.room_address} {self.room_rent}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    massage = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name}"


    
