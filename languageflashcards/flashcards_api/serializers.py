from rest_framework import serializers
from flashcards.models import Flashcard


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'word_class', 'word', 'definition', 'language', 'category', 'author', 'status',)
