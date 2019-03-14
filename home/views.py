from django.shortcuts import render

from django.apps import apps
from .models import PopularAnime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
importing_info = apps.get_model('info', 'Anime')
from django.apps import apps
importing_episode = apps.get_model('play', 'Episode')
# Create your views here.


def index(request,):
    anime_info = importing_info.objects.order_by('?')[:9]
    anime_top = importing_info.objects.order_by('-scores')[:9]
    popular = PopularAnime.objects.order_by('-id')[:9]
    random = importing_info.objects.order_by('?')[:15]
    random_search = importing_info.objects.order_by('?')[:1]
    episode = importing_episode.objects.order_by('-id')[:60]
    paginator = Paginator(episode, 12)
    page = request.GET.get('page')
    episode_data = paginator.get_page(page)
    context = {
        'random': random,
        'random_search': random_search,
        'episode_data': episode_data,
        'anime_info': anime_info,
        'popular': popular,
        'anime_top': anime_top,
    }
    return render(request, 'home/index.html', context)


def search(request):
    template = 'home/search.html'
    queryset_list = importing_info.objects.all()
    query = request.GET.get('q')
    if query == '':
        return HttpResponseRedirect('/')
    else:
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(tags__icontains=query) |
                Q(gener__icontains=query)
            ).order_by('-scores')
            random_search = importing_info.objects.order_by('?')[:1]
            paginator = Paginator(queryset_list, 30)
            page = request.GET.get('page')
            result = paginator.get_page(page)
            context = {
                'result': result,
                'random_search': random_search,
            }
            return render(request, template, context)
        else:
            messages.error(request, 'no results found')

    # if request.method == 'POST':
    #     query = request.POST['q']
    #     if query:
    #         match = importing_info.objects.filter(Q(name__icontains=query)).order_by('-scores')
    #         if match:
    #             paginator = Paginator(match, 12)
    #             page = request.GET.get('page')
    #             result = paginator.get_page(page)
    #             return render(request, template, {'result': result})
    #         else:
    #             messages.error(request, 'no results found')
    #     else:
    #         return HttpResponseRedirect('/')


def catlog(request, cat_item):
    template = 'home/catlog.html'
    queryset_list = importing_info.objects.all()
    query = cat_item
    if query == '':
        return HttpResponseRedirect('/')
    else:
        if query:
            queryset_list = queryset_list.filter(
                Q(gener__icontains=query)
            ).order_by('-scores')
            random_search = importing_info.objects.order_by('?')[:1]
            paginator = Paginator(queryset_list, 30)
            page = request.GET.get('page')
            result = paginator.get_page(page)
            context = {
                'result': result,
                'random_search': random_search,
            }
            return render(request, template, context)
        else:
            messages.error(request, 'no results found')


def error_404(request):
        anime_info = importing_info.objects.order_by('?')[:9]
        anime_top = importing_info.objects.order_by('-scores')[:9]
        popular = PopularAnime.objects.order_by('-id')[:9]
        random = importing_info.objects.order_by('?')[:15]
        random_search = importing_info.objects.order_by('?')[:1]
        episode = importing_episode.objects.order_by('-id')[:60]
        paginator = Paginator(episode, 12)
        page = request.GET.get('page')
        episode_data = paginator.get_page(page)
        context = {
            'random': random,
            'random_search': random_search,
            'episode_data': episode_data,
            'anime_info': anime_info,
            'popular': popular,
            'anime_top': anime_top,
        }
        return render(request, 'home/error404.html', context)
