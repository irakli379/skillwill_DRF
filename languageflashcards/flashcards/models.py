from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=99, unique=True)

    def __str__(self):
        return self.name


class WordClass(models.Model):
    options = (
        ('noun', 'Noun'),
        ('verb', 'Verb'),
        ('adjective', 'Adjective'),
        ('adverb', 'Adverb'),
    )

    name = models.CharField(max_length=99, choices=options, null=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=99,
                            unique=True,
                            help_text="Enter the language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name


class Flashcard(models.Model):

    # maybe not necessary
    # class FlashcardObjects(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(status='public')

    word_class = models.ForeignKey(WordClass, on_delete=models.PROTECT)

    word = models.CharField(max_length=99, unique=True)
    definition = models.TextField(max_length=333, unique=True)

    # maybe change on_delete later
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    # maybe change on_delete later
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    published = models.DateTimeField(default=timezone.now)

    options = (
        ('private', 'Private'),
        ('public', 'Public'),
    )

    status = models.CharField(max_length=15, choices=options, default='private')

    # maybe not necessary
    # objects = models.Manager()
    # flashcardobjects = FlashcardObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.word
