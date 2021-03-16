from django.urls import path
from .views import *

app_name = "quiz"

urlpatterns = [
    path('', QuizListView.as_view(), name = "quiz_list"),
    path('<int:pk>/', QuizDetailView.as_view(), name = "quiz_detail"),
    path('random/question/', QuestionRandomDetail.as_view(), name = 'quiz_random'),
]

