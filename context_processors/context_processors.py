from page_customisations.models import GlobalSiteStyling
from page_customisations.views import show_jumbotron_or_tiles


def global_styles_processor(request):
    return {
       'global_styles': GlobalSiteStyling.objects.all(),

    }
    
