from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"

    def validate_periodicity(self, value):  # field-level валидатор
        if not 1 <= value <= 7:
            raise serializers.ValidationError("Periodicity must be between 1 and 7 days.")
        return value

    def validate(self, attrs):  # object-level валидатор
        instance = self.instance

        reward = attrs.get("reward", instance.reward if instance else None)
        related_habit = attrs.get("related_habit", instance.related_habit if instance else None)
        is_pleasant = attrs.get("is_pleasant", instance.is_pleasant if instance else False)

        if reward and related_habit:  # нельзя вместе reward и related_habit
            raise serializers.ValidationError("You cannot specify both reward and related habit.")

        if related_habit and not related_habit.is_pleasant:  # связанная привычка д.б. приятной
            raise serializers.ValidationError("Related habit must be pleasant.")

        if is_pleasant and (reward or related_habit):  # приятная привычка не м. иметь награды
            raise serializers.ValidationError("Pleasant habit cannot have reward or related habit.")

        return attrs

