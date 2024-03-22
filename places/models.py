from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator




class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio=models.CharField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class PlaceOwner(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.place.name} owned by {self.owner}"



class Comment(models.Model):
    coment_text = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    stars_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return f"{self.user} comment to  {self.place.name}"



