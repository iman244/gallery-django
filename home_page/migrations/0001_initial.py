# Generated by Django 5.1.2 on 2024-10-18 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='', verbose_name='cover')),
                ('title', models.CharField(max_length=1000, verbose_name='title')),
                ('description', models.TextField(max_length=2000, verbose_name='description')),
                ('second_description', models.TextField(max_length=2000, verbose_name='second description')),
                ('some_works_button_text', models.CharField(max_length=1000, verbose_name='some works button text')),
                ('about_button_text', models.CharField(max_length=1000, verbose_name='about works button text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('link', models.URLField(verbose_name='your social media link')),
                ('page', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home_page.homepage')),
            ],
        ),
    ]
