# Generated by Django 3.2.7 on 2021-09-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_alter_answer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='image',
            new_name='answer_image',
        ),
    ]