# Generated by Django 3.0.2 on 2020-02-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_inquir',
            name='australia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person_inquir',
            name='canada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person_inquir',
            name='united_kingdom',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person_inquir',
            name='usa',
            field=models.BooleanField(default=False),
        ),
    ]
