from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer


class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.order_by("-wpm")[:10]
    serializer_class = ScoreSerializer