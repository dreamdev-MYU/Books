from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):
    LANGUAGE_CHOICES = [
        ('ru', 'Russian'),
        ('en', 'English'),
        ('uz', 'Uzbek'),
    ]
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="book_images/")
    description = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


    
class Owner(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    bio=models.TextField()

    
    def __str__(self):
        return self.first_name
    
class BooksOwner(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.book}ning muallifi {self.owner}"

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE, related_name ="reviews")
    comment_text=models.TextField()
    stars_given=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) 
    created_at = models.DateField(default= timezone.now)
    
    def __str__(self):
        return f"{self.user} comment to {self.book} and give {self.stars_given} stars"