# Generated by Django 4.1.2 on 2022-10-13 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registertable',
            old_name='Name',
            new_name='Email',
        ),
    ]
