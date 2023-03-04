from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Animal, Species
from django.utils import timezone


class AnimalPopulationView(View):
    def get(self, request):
        animals_number = Animal.objects.all().count()
        return HttpResponse('Total Animals = ' + str(animals_number))


class AnimalView(View):
    def get(self, request):
        animal_name = request.GET.get('name')
        try:
            animal_object = Animal.objects.get(name=animal_name)
        except Animal.DoesNotExist:
            return HttpResponse(status=404)
        returned_data = {
            "name": animal_object.name,
            "species": animal_object.species.name,
            "last_feed_time": animal_object.last_feed_time.isoformat(),
        }
        return JsonResponse(returned_data)

    def post(self, request):
        animal_name = request.POST.get('name')
        animal_species = request.POST.get('species')
        if len(animal_name) > 30 or len(animal_species) > 30:
            return HttpResponse(status=400)
        try:
            animal_obj = Animal.objects.get(name=animal_name)
            return HttpResponse('Already Exists!!', status=422)
        except:
            species_obj, _ = Species.objects.get_or_create(name=animal_species)
            animal_obj = Animal.objects.create(name=animal_name, species=species_obj)
            returned_data = {
                "name": animal_obj.name,
                "species": animal_obj.species.name,
                "last_feed_time": animal_obj.last_feed_time.isoformat(),
            }
            return JsonResponse(data=returned_data, status=201)


class HungryAnimalsView(View):
    def get(self, request):
        date_from_two_days = timezone.now() - timezone.timedelta(days=2)
        animals_number = Animal.objects.filter(last_feed_time__lte=date_from_two_days)
        return HttpResponse('Animals hungry = ' + str(animals_number.count()))


class FeedAnimalView(View):
    def post(self, request):
        animal_name = request.POST.get('name')
        try:
            animal_obj = Animal.objects.get(name=animal_name)
        except Animal.DoesNotExist:
            return HttpResponse(status=404)
        animal_obj.last_feed_time = timezone.now()
        animal_obj.save()
        return HttpResponse('Animal Fed Successfully')
