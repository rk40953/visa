# Generated by Django 3.0.2 on 2020-02-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person_inquir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=85)),
                ('last_name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=500)),
                ('usa', models.BooleanField(default=True)),
                ('australia', models.BooleanField(default=True)),
                ('canada', models.BooleanField(default=True)),
                ('united_kingdom', models.BooleanField(default=True)),
            ],
        ),
    ]
