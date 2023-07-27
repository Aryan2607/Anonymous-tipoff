# Generated by Django 3.2.9 on 2021-12-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_delete_tipoffmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoff',
            name='Age',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Educational_Qualification',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Gender',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Got_Information_About_Case',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoff',
            name='Relation_to_Suspect_or_Victim',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
