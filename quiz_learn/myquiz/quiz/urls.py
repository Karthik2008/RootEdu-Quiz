from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('contact/', views.contact, name='quiz-contact'),
    path('list/', views.quizlist, name='quiz-list'),
    path('linux/', views.linuxquiz, name='linux-quiz'),
    path('correct/', views.correct, name='quiz-correct'),
    path('wrong/', views.wrong, name='quiz-wrong'),
]