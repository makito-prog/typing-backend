from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "player_name", "wpm", "accuracy", "created_at"]
        read_only_fields = ["id", "created_at"]