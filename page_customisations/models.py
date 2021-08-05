from django.db import models


class GlobalSiteStyling(models.Model):
    styling_name = models.CharField(default='Styling name', max_length=100)
    show_tiles = models.BooleanField(default=False)
    show_jumbotron = models.BooleanField(default=False)
    
    class Meta:
            verbose_name_plural = 'Global Page Styles'
        
    def __str__(self):
        return self.styling_name


