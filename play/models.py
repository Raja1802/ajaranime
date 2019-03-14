from django.db import models
from datetime import datetime


class Episode(models.Model):
    class Meta:
        db_table = 'episode'
    anime = models.ForeignKey('info.Anime', on_delete=models.CASCADE, default=1)
    name_anime = models.CharField(max_length=200, null=True, blank=True)
    episode = models.CharField(max_length=200, null=True, blank=True)
    download_url = models.CharField(max_length=300, null=True, blank=True)
    server_1 = models.CharField(max_length=300, null=True, blank=True)
    server_2 = models.CharField(max_length=300, null=True, blank=True)
    server_3 = models.CharField(max_length=300, null=True, blank=True)
    server_4 = models.CharField(max_length=300, null=True, blank=True)
    server_5 = models.CharField(max_length=300, null=True, blank=True)
    server_6 = models.CharField(max_length=300, null=True, blank=True)
    server_7 = models.CharField(max_length=300, null=True, blank=True)
    server_8 = models.CharField(max_length=300, null=True, blank=True)
    server_9 = models.CharField(max_length=300, null=True, blank=True)
    # time_added = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    # episode_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.episode


