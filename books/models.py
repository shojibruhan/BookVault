from django.db import models
from users.models import Author
# Create your models here.

class Genre(models.Model):
    MISCELLANEOUS= 'Miscellaneous'
    CLASSICS= 'Classics'
    THRILLER= 'Thriller'
    FANTASY= 'Fantasy'
    ADVENTURE= 'Adventure'
    SELF_HELP= 'Self_help'
    HORROR= 'Horror'
    GENRE_CHOICES= [
        (MISCELLANEOUS, 'Pending'),
        (CLASSICS, 'Classics'),
        (THRILLER, 'Thriller'),
        (FANTASY, 'Fantasy'),
        (ADVENTURE, 'Adventure'),
        (SELF_HELP, 'Self_help'),
        (HORROR, 'Horror'),
    ]
   

    genre= models.CharField(max_length=30,
                            choices=GENRE_CHOICES,
                            default=MISCELLANEOUS)

    def __str__(self):
        return self.genre

class Book(models.Model):
    title= models.CharField(max_length=250)
    author= models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn= models.IntegerField(unique=True)
    genre= models.ManyToManyField(Genre, related_name='books')
    availability_status=models.BooleanField(default= True)

    def __str__(self):
        return self.title




