from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flashcards.urls', namespace='flashcards')),
    path('api/', include('flashcards_api.urls', namespace='flashcards_api')),
]
