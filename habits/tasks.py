from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from telegram_bot.bot import send_message


@shared_task
def send_habit_reminders():
    now = timezone.localtime()
    current_time = now.time().replace(second=0, microsecond=0)

    habits = Habit.objects.filter(time=current_time)

    for habit in habits:
        user = habit.owner

        if not user or not user.telegram_chat_id:
            continue

        message = f"Reminder:\n{habit.action} at {habit.time}"

        send_message(user.telegram_chat_id, message)
