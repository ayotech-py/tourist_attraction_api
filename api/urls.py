from django.urls import path
from .views import UserInputView

urlpatterns = [
    path('userinput/', UserInputView.as_view()),
]
