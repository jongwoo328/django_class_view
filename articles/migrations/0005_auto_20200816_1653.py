# Generated by Django 2.2 on 2020-08-16 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200816_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aticle',
            new_name='article',
        ),
    ]