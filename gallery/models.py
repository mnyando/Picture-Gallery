from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(upload_to = 'photos/')