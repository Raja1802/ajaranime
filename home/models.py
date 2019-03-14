from django.db import models


class PopularAnime(models.Model):
    class Meta:
        db_table = 'popular'
    cover = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    anime_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
