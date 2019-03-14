from django.db import models


class Schedule(models.Model):
        class Meta:
            db_table = 'schedule'
        schedule_anime_name = models.CharField(max_length=300, null=True, blank=True)
        schedule_anime_image = models.CharField(max_length=300, null=True, blank=True)
        schedule_anime_day = models.CharField(max_length=50, null=True, blank=True)
        schedule_anime_date = models.CharField(max_length=20, null=True, blank=True)
        schedule_anime_episode = models.CharField(max_length=30, null=True, blank=True)
        schedule_anime_time = models.CharField(max_length=50, null=True, blank=True)
        schedule_anime_month = models.CharField(max_length=100, null=True, blank=True)
        schedule_anime_year = models.CharField(max_length=100, null=True, blank=True)
        schedule_anime_week_number = models.CharField(max_length=50, null=True, blank=True)
        schedule_anime_fanrelated = models.CharField(max_length=10, null=True, blank=True)
        anime_info_id = models.CharField(max_length=100, null=True, blank=True)

        def __str__(self):
            template = '{0.schedule_anime_name}'
            return template.format(self)
