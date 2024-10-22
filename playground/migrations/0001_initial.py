# Generated by Django 5.0.7 on 2024-08-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('show_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('cast_members', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_added', models.DateField()),
                ('release_year', models.IntegerField()),
                ('rating', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('listed_in', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
