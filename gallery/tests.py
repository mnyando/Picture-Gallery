from django.test import TestCase
from .models import Tag, Photos, Location, Category
import datetime as dt

# Create your tests here.
class TagTestCase(TestCase):
    def setUp(self):
        self.life = Tag(name='life')

    def test_instance(self):
        self.assertTrue(isinstance(self.life, Tag))

class LocationTest(TestCase):
    def setUp(self):
        '''new instance before test'''
        self.ny = Location(name='ny')

    def tearDown(self):
        Location.objects.all().delete()

    def test_location_instance(self):
        self.assertTrue(isinstance(self.ny, Location))

    def test_save_location(self):
        self.ny.save_location()
        location = Location.objects.all()
        self.assertEqual(len(location), 1)

    def test_update_location(self):
        self.ny.save_location()
        self.ny.update_location(self.ny.id,'kenya')
        update = Location.objects.get(name = "kenya")
        self.assertEqual(update.name, 'kenya')

class CategoryTest(TestCase):
    def setUp(self):
        
        self.fun = Category(name = "fun")

    def tearDown(self):
        
        Category.objects.all().delete()

    def test_category_instance(self):
        
        self.assertTrue(isinstance(self.fun, Category))

    def test_save_category_method(self):
        self.fun.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 1)

    def test_delete_category(self):
        self.fun.save_category()
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),1)
        self.fun.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),0)

    def test_update_category(self):
        
        self.fun.save_category()
        self.fun.update_category(self.fun.id,'sports')
        update = Category.objects.get(name = "sports")
        self.assertEqual(update.name, 'sports')

class PhotosTestClass(TestCase):
    def setUp(self):
    
        self.fun = Category( name= "fun")
        self.ny = Location (name = "ny")
        self.art = Photos(photo_image = "art.jpg", name ='art', description = 'artistic', category= self.fun, location= self.ny)

    def tearDown(self):
       
        Photos.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_photo_instance(self):
       
        self.assertTrue(isinstance(self.art, Photos))

    def test_image_instance(self):
        
        self.assertTrue(isinstance(self.art, Photos))