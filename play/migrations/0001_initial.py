# Generated by Django 2.1.7 on 2019-03-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_anime', models.CharField(blank=True, max_length=200, null=True)),
                ('episode', models.CharField(blank=True, max_length=200, null=True)),
                ('download_url', models.CharField(blank=True, max_length=300, null=True)),
                ('server_1', models.CharField(blank=True, max_length=300, null=True)),
                ('server_2', models.CharField(blank=True, max_length=300, null=True)),
                ('server_3', models.CharField(blank=True, max_length=300, null=True)),
                ('server_4', models.CharField(blank=True, max_length=300, null=True)),
                ('server_5', models.CharField(blank=True, max_length=300, null=True)),
                ('server_6', models.CharField(blank=True, max_length=300, null=True)),
                ('server_7', models.CharField(blank=True, max_length=300, null=True)),
                ('server_8', models.CharField(blank=True, max_length=300, null=True)),
                ('server_9', models.CharField(blank=True, max_length=300, null=True)),
                ('anime', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.Anime')),
            ],
            options={
                'db_table': 'episode',
            },
        ),
    ]
