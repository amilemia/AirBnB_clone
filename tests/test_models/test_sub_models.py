#!/usr/bin/python3
"""test_sub_modeles module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestNewClasses(unittest.TestCase):
    """Test cases for the sub classes"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_user(self):
        """Test the User class"""
        my_user = User()
        my_user.first_name = "Khaled"
        my_user.last_name = "Ibn Al-Walid"
        my_user.email = "unbeatable@leader.war"
        my_user.password = "TheSwordOfGod"
        my_user.save()

        all_objs = self.storage.all()
        key = f'User.{my_user.id}'
        self.assertIn(key, all_objs.keys())

    def test_state(self):
        """Test the State class"""
        my_state = State()
        my_state.name = "Tanger-Tetouan-Al Hoceima"
        my_state.save()

        all_objs = self.storage.all()
        key = f'State.{my_state.id}'
        self.assertIn(key, all_objs.keys())

    def test_city(self):
        """Test the City class"""
        my_city = City()
        my_city.state_id = "R"
        my_city.name = "Al Hoceima"
        my_city.save()

        all_objs = self.storage.all()
        key = f'City.{my_city.id}'
        self.assertIn(key, all_objs.keys())

    def test_amenity(self):
        """Test the Amenity class"""
        my_amenity = Amenity()
        my_amenity.name = "Wifi"
        my_amenity.save()

        all_objs = self.storage.all()
        key = f'Amenity.{my_amenity.id}'
