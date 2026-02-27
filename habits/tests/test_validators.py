from django.test import TestCase
from django.contrib.auth import get_user_model

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitValidatorTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345"
        )

        self.pleasant_habit = Habit.objects.create(
            owner=self.user,
            action="Drink tea",
            time="08:00",
            duration=60,
            is_pleasant=True
        )

    def test_cannot_have_reward_and_related_habit(self):
        data = {
            "place": "home",
            "time": "09:00",
            "action": "Read book",
            "is_pleasant": False,
            "reward": "Coffee",
            "related_habit": self.pleasant_habit.id,
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("You cannot specify both reward and related habit.", str(serializer.errors))

    def test_related_habit_must_be_pleasant(self):
        bad_habit = Habit.objects.create(
            owner=self.user,
            action="Go jogging",
            time="07:00",
            duration=60,
            is_pleasant=False
        )

        data = {
            "place": "park",
            "time": "08:00",
            "action": "Stretch",
            "is_pleasant": False,
            "related_habit": bad_habit.id,
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Related habit must be pleasant.", str(serializer.errors))

    def test_pleasant_habit_cannot_have_reward(self):
        data = {
            "place": "home",
            "time": "10:00",
            "action": "Watch movie",
            "is_pleasant": True,
            "reward": "Popcorn",
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Pleasant habit cannot have reward or related habit.", str(serializer.errors),)

    def test_periodicity_must_be_between_1_and_7(self):
        data = {
            "place": "home",
            "time": "11:00",
            "action": "Meditate",
            "is_pleasant": False,
            "periodicity": 10,
            "duration": 60,
            "is_public": False,
        }

        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Periodicity must be between 1 and 7 days.", str(serializer.errors))

    def test_valid_habit(self):
        data = {
            "place": "home",
            "time": "12:00",
            "action": "Read",
            "is_pleasant": False,
            "related_habit": self.pleasant_habit.id,
            "periodicity": 1,
            "duration": 60,
            "is_public": True,
        }

        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid())
