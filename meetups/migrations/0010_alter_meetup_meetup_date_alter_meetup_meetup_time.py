# Generated by Django 4.0.4 on 2022-07-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0009_meetup_from_date_meetup_meetup_time_meetup_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='meetup_time',
            field=models.TimeField(),
        ),
    ]
