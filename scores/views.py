from django.http import JsonResponse
from .models import Score

def ranking(request):
    scores = Score.objects.order_by("-wpm")[:10]
    data = [
        {
            "id": s.id,
            "player_name": s.player_name,
            "wpm": s.wpm,
            "accuracy": s.accuracy,
            "created_at": s.created_at,
        }
        for s in scores
    ]
    return JsonResponse(data, safe=False)