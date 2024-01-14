from django.urls import path
from .views import FlashcardsList, FlashcardsDetail

app_name = 'flashcards_api'

urlpatterns = [
    path('<int:pk>', FlashcardsDetail.as_view(), name='detailcreate'),
    path('', FlashcardsList.as_view(), name='listcreate'),
]