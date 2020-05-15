# Generated by Django 3.0.6 on 2020-05-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_end_year', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('win', models.BooleanField()),
                ('home', models.BooleanField()),
                ('oppt', models.CharField(max_length=3)),
                ('points_for', models.PositiveIntegerField()),
                ('points_against', models.PositiveIntegerField()),
            ],
        ),
    ]