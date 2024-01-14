from rest_framework import generics
from flashcards.models import Flashcard
from .serializers import FlashcardSerializer


class FlashcardsList(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class FlashcardsDetail(generics.RetrieveDestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
