# Generated by Django 5.1.2 on 2024-10-19 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(db_index=True, max_length=100)),
                ('receipe_description', models.TextField()),
                ('receipe_image', models.ImageField(upload_to='recepie/')),
                ('receipe_slug', models.SlugField(unique=True)),
                ('receipe_type', models.CharField(choices=[('veg', 'veg'), ('non-veg', 'non-veg')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients_name', models.CharField(max_length=100)),
                ('receipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipe_ingredients', to='home.receipe')),
            ],
        ),
    ]
