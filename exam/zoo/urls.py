from django.urls import path
from .views import AnimalPopulationView, AnimalView, HungryAnimalsView, FeedAnimalView

urlpatterns = [
    path('total/', AnimalPopulationView.as_view(), name='animal population'),
    path('animal/', AnimalView.as_view(), name='animal'),
    path('animal/<slug:name>', AnimalView.as_view(), name='animal'),
    path('hungry/', HungryAnimalsView.as_view(), name='hungry animals'),
    path('feed/', FeedAnimalView.as_view(), name='feed animals'),
]
