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
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(upload_to = 'photos/')

    def save_photo(self):
        self.save()

    def __str__(self):
        return self.name

    def delete_photo(self):
        self.delete()
        

    @classmethod
    def search_by_category(cls,search_term):
        album = cls.objects.filter(category__name__icontains=search_term)
        return album

    @classmethod
    def todays_album(cls):
        # today = dt.date.today()
        album = cls.objects.filter()
        return album

    @classmethod
    def get_album_by_id(cls, id):
        album_id = cls.objects.get(id=id)
        return album_id
    def album_id(self):
        self.copy()

    @classmethod
    def filter_by_location(cls,location):
        searched = Location.objects.get(name = location)
        album = Photos.objects.filter(location = searched.id)
        return album 

    @classmethod
    def display_all_photos(cls):
        return cls.objects.all()