# Generated by Django 4.0.4 on 2022-07-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_speaker_meetup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
