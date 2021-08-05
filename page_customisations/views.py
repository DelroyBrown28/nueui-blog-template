from django.shortcuts import render
from .models import GlobalSiteStyling



def show_jumbotron_or_tiles(request):
    show_jumbotron_or_tiles = JumbotronOrTiles.objects.all()
    context = {
        'show_jumbotron_or_tiles' : show_jumbotron_or_tiles,
    }
    return render(request, 'blog/index.html', context)

