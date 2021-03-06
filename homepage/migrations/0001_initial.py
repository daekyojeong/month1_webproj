# Generated by Django 3.1.4 on 2020-12-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTT',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=120)),
                ('year', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0, null=True)),
                ('imdb', models.FloatField(default=0, null=True)),
                ('rotten_tomatoes', models.FloatField(default=0, null=True)),
                ('netflix', models.BooleanField(default=False)),
                ('hulu', models.BooleanField(default=False)),
                ('primevideo', models.BooleanField(default=False)),
                ('disneyplus', models.BooleanField(default=False)),
                ('direcrtors', models.CharField(default='', max_length=500, null=True)),
                ('genres', models.CharField(default='', max_length=100, null=True)),
                ('country', models.CharField(default='', max_length=300, null=True)),
                ('language', models.CharField(default='', max_length=100, null=True)),
                ('runtime', models.FloatField(default=0, null=True)),
            ],
        ),
    ]
