from django.contrib import admin
from . import models
from page_customisations.models import GlobalSiteStyling
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin
from tinymce.widgets import TinyMCE



class JumbotronTiles(admin.ModelAdmin):
    list_display = (
        'styling_name',
        'show_tiles',
        'show_jumbotron',
    )
    list_display_links = (
        'styling_name',
    ) 
    list_editable = (
        'show_tiles',
        'show_jumbotron',
    )

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'add_to_carousel', 'category', 'id', 'status', 'author')
    list_editable = ('status', 'category', 'add_to_carousel')
    prepopulated_fields = {
        "slug" : ("title",),
    }
    readonly_fields = (
        'favorites',
        'likes',
        'thumbsup',
        'thumbsdown',
        'thumbs',
        'published',
        )
    # formfield_overrides = {
    # models.Post.content: {'widget': TinyMCE()}
    # }
 
@admin.register(models.Vote)    
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'vote')
    # list_editable = ()
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("name",),
    }
    
    
admin.site.register(models.Comment, MPTTModelAdmin)
admin.site.register(GlobalSiteStyling, JumbotronTiles)
