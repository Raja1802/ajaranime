from django.shortcuts import render
from django.http import Http404
from .models import Anime
from django.apps import apps
from django.core.paginator import Paginator
importing_info = apps.get_model('play', 'Episode')


def info(request, id_anime):
    try:
        data = Anime.objects.get(id=id_anime)
    except Anime.DoesNotExist:
        raise Http404("not exist")
    random_search = Anime.objects.order_by('?')[:1]
    episode_data = data.episode_set.order_by('-id')
    paginator = Paginator(episode_data, 12)
    page = request.GET.get('page')
    episode_data = paginator.get_page(page)
    recomendations = Anime.objects.order_by('?')[:8]
    context = {
        'episode_data': episode_data,
        'data': data,
        'recom': recomendations,
        'random_search': random_search,
    }
    return render(request, 'info/info.html', context)

