# Generated by Django 2.1.4 on 2019-01-02 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='athor',
            new_name='author',
        ),
    ]
