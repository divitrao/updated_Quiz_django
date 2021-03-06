from django.urls import path
from .views import QuizzList 
from .views import PlayQuiz,  Result, updateTime 

app_name = 'QuizApp'

urlpatterns = [
                path('quizlist/',QuizzList.as_view(),name='quizlist'),
                path('<slug>/',PlayQuiz.as_view(),name='playquiz'),
                path('<result>/<slugs>/', Result.as_view(), name='result'),
                path('timeupdate',updateTime.as_view(),name='timeupdates'),]

