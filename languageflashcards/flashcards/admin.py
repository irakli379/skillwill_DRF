from django.contrib import admin
from .models import Flashcard, WordClass, Language, Category
# from .models import WordClass


# @admin.register(models.Flashcard)
# class AuthorAdmin(admin.ModelAdmin)

admin.site.register(WordClass),
admin.site.register(Flashcard),
admin.site.register(Language),
admin.site.register(Category),

