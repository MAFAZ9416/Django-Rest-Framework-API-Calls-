from django.urls import path
from .views import *

# path creation 

urlpatterns = [
    path('api/', StudentAPI.as_view()),
    path('api/<int:student_id>/', StudentAPI.as_view()),

    path('task/', TaskView.as_view()),
    path('task/<int:task_id>/', TaskView.as_view()),

    path('rank/', RankSheetView.as_view()),
    path('rank/<int:rank_id>/', RankSheetView.as_view()),

    path('task_fun/',API),
    path('task_fun/<int:id>/',API)
]