from django.urls import path
from .views import *

urlpatterns = [
    path('server/<slug:cpu>', cpu_server, name='cpu_server'),
    path('', Result.as_view(), name='result'),
    path('results', Result.as_view(), name='result'),
    path('results_last_100', Last100Results.as_view(), name='last100'),
    path('results_last_100_min', Last100ResultsMin.as_view(), name='last100min'),
    path('results_last_100_max', Last100ResultsMax.as_view(), name='last100max'),
    path('results_min', ResultMin.as_view(), name='allmin'),
    path('results_max', ResultMax.as_view(), name='allmax'),
]