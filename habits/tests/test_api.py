from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from habits.models import Habit


class HabitAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username="user1", password="12345")
        self.user2 = get_user_model().objects.create_user(username="user2", password="12345")

        self.habit_user1 = Habit.objects.create(
            owner=self.user1,
            action="Read",
            time="08:00",
            duration=60,
            is_pleasant=True,
        )

        self.habit_user2 = Habit.objects.create(
            owner=self.user2,
            action="Run",
            time="09:00",
            duration=60,
            is_pleasant=True,
        )

        self.client.force_authenticate(user=self.user1)

    def test_user_sees_only_own_habits(self):
        response = self.client.get("/api/habits/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["id"], self.habit_user1.id)

    def test_user_cannot_access_habit_of_other_user(self):
        response = self.client.get(f"/api/habits/{self.habit_user2.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_is_set_automatically_on_create(self):
        data = {
            "place": "home",
            "action": "Drink water",
            "time": "10:00",
            "duration": 60,
            "is_pleasant": False,
            "periodicity": 1,
            "is_public": False,
        }

        response = self.client.post("/api/habits/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["owner"], self.user1.id)

    def test_public_habits_list(self):
        public_habit = Habit.objects.create(
            owner=self.user2,
            action="Smile",
            time="11:00",
            duration=60,
            is_pleasant=True,
            is_public=True,
        )

        response = self.client.get("/api/habits/public/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["id"], public_habit.id)

    def test_cannot_create_public_habit_via_public_endpoint(self):
        response = self.client.post("/api/habits/public/", {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
