from django.test import TestCase
from django.contrib.auth import get_user_model

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitSerializerTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="user1", password="12345")

        self.other_user = get_user_model().objects.create_user(username="user2", password="12345")

    def test_owner_is_read_only(self):
        data = {
            "owner": self.other_user.id,  # пытаемся подменить
            "place": "home",
            "time": "08:00",
            "action": "Drink water",
            "is_pleasant": True,
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_owner_is_set_automatically(self):
        data = {
            "place": "home",
            "time": "09:00",
            "action": "Read book",
            "is_pleasant": True,
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        habit = serializer.save(owner=self.user)

        self.assertEqual(habit.owner, self.user)

    def test_owner_is_present_in_output(self):
        habit = Habit.objects.create(
            owner=self.user,
            action="Stretch",
            time="07:00",
            duration=60,
            is_pleasant=True,
        )

        serializer = HabitSerializer(habit)
        self.assertEqual(serializer.data["owner"], self.user.id)
