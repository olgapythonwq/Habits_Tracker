from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator


class Habit(models.Model):
    # 1. Связи
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits",
                              verbose_name="Owner")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name="related_to", verbose_name="Related habit")
    # 2. Основные данные привычки
    place = models.CharField(max_length=255, verbose_name="Place")
    time = models.TimeField(verbose_name="Time")
    action = models.CharField(max_length=255, verbose_name="Action")
    # 3. Бизнес-логика
    is_pleasant = models.BooleanField(default=False, verbose_name="Is pleasant")
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name="Reward", help_text="Enter reward")
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="Periodicity (days)")
    duration = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120)], verbose_name="Duration (seconds)")
    is_public = models.BooleanField(default=False, verbose_name="Is public")
    # 4. Служебные поля
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"

    def __str__(self):
        return f"{self.action} at {self.time}"
