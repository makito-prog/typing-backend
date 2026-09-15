from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=20)
    wpm = models.PositiveIntegerField()
    accuracy = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name}: {self.wpm} WPM"