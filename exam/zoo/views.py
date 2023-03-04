from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Animal, Species
from datetime import datetime, timedelta
from django.utils import timezone


class AnimalPopulationView(generic.View):
    def get(self, request):
        animals_number = Animal.objects.all().count()
        return HttpResponse('Total Animals = ' + str(animals_number))


class AnimalView(generic.View):
    def get(self, request, name):
        animal_object = get_object_or_404(Animal, name=name)
        returned_data = {
            "name": animal_object.name,
            "species": animal_object.species.name,
            "last_feed_time": animal_object.last_feed_time
        }
        return JsonResponse(data=returned_data)

    def post(self, request, format=None):
        animal_name = request.POST.get('name')
        animal_species = request.POST.get('species')

        check_species = Species.objects.filter(name=animal_species)
        if check_species.count() <= 0:
            Species.objects.create(name=animal_species)
        species_obj = Species.objects.get(name=animal_species)
        animal_obj = Animal.objects.create(name=animal_name, species=species_obj)
        if animal_obj:
            returned_data = {
                "name": animal_obj.name,
                "species": animal_obj.species.name,
                "last_feed_time": animal_obj.last_feed_time
            }
            return JsonResponse(data=returned_data, status=201)
        else:
            return JsonResponse(status=422)


class HungryAnimalsView(generic.View):
    def get(self, request):
        date_from_two_days = timezone.now() - timedelta(days=2)
        animals_number = Animal.objects.filter(last_feed_time__lte=date_from_two_days)
        return HttpResponse('Animals hungry = ' + str(animals_number.count()))


class FeedAnimalView(generic.View):
    def post(self, request):
        animal_name = request.POST.get('name')
        animal_obj = Animal.objects.get(name=animal_name)
        animal_obj.last_feed_time = timezone.now()
        animal_obj.save()
        return HttpResponse('Updated Successfully')
