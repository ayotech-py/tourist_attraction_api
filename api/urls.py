from django.urls import path
from .views import LocInputView, BudgetInputView, TypeInputView, TypeRadiusInputView

urlpatterns = [
    path('tourist_attraction/', LocInputView.as_view()),
    path('tourist_budget/', BudgetInputView.as_view()),
    path('tourist_type/', TypeInputView.as_view()),
    path('tourist_type_radius/', TypeRadiusInputView.as_view()),
]
