# Generated by Django 3.2.12 on 2023-06-30 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.CharField(max_length=100, null=True)),
                ('is_bestselling', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
