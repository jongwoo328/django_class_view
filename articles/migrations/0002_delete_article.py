# Generated by Django 2.2 on 2020-08-15 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]