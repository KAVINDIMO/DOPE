# Generated by Django 3.1.1 on 2020-09-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_vegan_vegetarian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ketogenic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('calories', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('protiens', models.FloatField()),
                ('fat', models.FloatField()),
            ],
        ),
    ]