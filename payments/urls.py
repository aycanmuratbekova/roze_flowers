from django.urls import path
from .views import TransactionView, TransactionSuccessView, FailureView


urlpatterns = [
    path('transaction/', TransactionView.as_view()),
    path('transaction/success/', TransactionSuccessView.as_view()),
    path('transaction/failure/', FailureView.as_view()),
]
