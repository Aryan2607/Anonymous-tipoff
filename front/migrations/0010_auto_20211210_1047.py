# Generated by Django 3.2.9 on 2021-12-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_tipoff_listed_cases'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoff',
            name='Death_or_Loss_in_Family',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Disruption_in_Studies',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Disruption_of_Intimate_Relationships',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Faced_any_Violence',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Family_Member_is_not_healthy',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Provided_information_to_Police_or_Justice_System',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
