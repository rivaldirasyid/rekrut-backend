from django.urls import path
from .views import KandidatList, KriteriaList, SAWCalculator

urlpatterns = [
    path('kandidat/', KandidatList.as_view(), name='kandidat-list'),
    path('kriteria/', KriteriaList.as_view(), name='kriteria-list'),
    path('saw/', SAWCalculator.as_view(), name='saw-calculator'),
]
