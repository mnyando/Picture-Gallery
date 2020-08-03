from django.test import TestCase
from .models import Tag, Photos, Location, Category
import datetime as dt

# Create your tests here.
class TagTestCase(TestCase):
    def setUp(self):
        self.life = Tag(name='life')

    def test_instance(self):
        self.assertTrue(isinstance(self.life, Tag))