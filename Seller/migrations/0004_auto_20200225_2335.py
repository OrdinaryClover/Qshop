# Generated by Django 2.2.1 on 2020-02-25 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_loginuser_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='phone',
            new_name='phono',
        ),
    ]
