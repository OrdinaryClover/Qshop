# Generated by Django 2.2.1 on 2020-02-25 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0004_auto_20200225_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='phono',
            new_name='photo',
        ),
    ]
