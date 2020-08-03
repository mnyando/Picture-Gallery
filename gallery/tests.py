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
        self.nairobi = Location(name='nairobi')

    def tearDown(self):
        Location.objects.all().delete()

    def test_location_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_location(self):
        self.nairobi.save_location()
        location = Location.objects.all()
        self.assertEqual(len(location), 1)

    def test_update_location(self):
        self.nairobi.save_location()
        self.nairobi.update_location(self.nairobi.id,'maldives')
        update = Location.objects.get(name = "maldives")
        self.assertEqual(update.name, 'maldives')