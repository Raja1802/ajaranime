from django.shortcuts import render
from django.http import Http404
from .models import Episode
from django.core.paginator import Paginator
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
# Create your views here.


def play(request, episode_id, id_anime):
    try:
       data = importing_info.objects.get(id=id_anime)
    except importing_info.DoesNotExist:
        raise Http404("Anime does not exist")
    random_search = importing_info.objects.order_by('?')[:1]
    episode_data = data.episode_set.order_by('-id')
    paginator = Paginator(episode_data, 12)
    page = request.GET.get('page')
    episode_data = paginator.get_page(page)
    anime_info = importing_info.objects.get(id=id_anime)
    random = importing_info.objects.order_by('?')[:15]
    try:
        episode = Episode.objects.get(id=episode_id)
    except episode.DoesNotExist:
        raise Http404("Anime does not exist")
    context = {
        'anime_info': anime_info,
        'random': random,
        'episode': episode,
        'episode_data': episode_data,
        'random_search': random_search,
    }
    return render(request, 'play/play.html', context)




