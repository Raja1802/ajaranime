from django.shortcuts import render
from .models import Schedule
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
from django.apps import apps
importing_episode = apps.get_model('play', 'Episode')
# Create your views here.


def schedule(request):
     schedule_data = Schedule.objects.order_by('-id')
     random_search = importing_info.objects.order_by('?')[:1]
     context = {
         'schedule_data': schedule_data,
         'random_search': random_search,
     }
     return render(request, 'schedule/schedule.html', context)
