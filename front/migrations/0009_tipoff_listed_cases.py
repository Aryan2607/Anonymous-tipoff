# Generated by Django 3.2.9 on 2021-12-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_tipoff_existing_or_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoff',
            name='Listed_Cases',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
