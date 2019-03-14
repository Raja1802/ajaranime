from django.shortcuts import render
from django.apps import apps
from django.core.paginator import Paginator
importing_info = apps.get_model('info', 'Anime')
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


def anime(request):
    anime_info = importing_info.objects.order_by('-scores')
    random_search = importing_info.objects.order_by('?')[:1]
    paginator = Paginator(anime_info, 42)
    page = request.GET.get('page')
    anime_data = paginator.get_page(page)
    context = {
        'anime_data': anime_data,
        'random_search': random_search,
    }
    return render(request, 'anime/anime.html', context)


def sort(request, sort_query):
    template = 'anime/anime.html'
    sort = importing_info.objects.order_by(sort_query)
    random_search = importing_info.objects.order_by('?')[:1]
    paginator = Paginator(sort, 42)
    page = request.GET.get('page')
    anime_data = paginator.get_page(page)
    context = {
        'anime_data': anime_data,
        'random_search': random_search,
    }
    return render(request, template, context)

def filter(request, filter_query):
    template = 'anime/anime.html'
    queryset_list = importing_info.objects.all()
    query = filter_query
    if query == '':
        return HttpResponseRedirect('/')
    else:
        if query:
            queryset_list = queryset_list.filter(
                Q(types__icontains=query)
            ).order_by('-scores')
            paginator = Paginator(queryset_list, 42)
            random_search = importing_info.objects.order_by('?')[:1]
            page = request.GET.get('page')
            result = paginator.get_page(page)
            context = {
                'anime_data': result,
                'random_search': random_search,
            }
            return render(request, template, context)
        else:
            messages.error(request, 'no results found')
