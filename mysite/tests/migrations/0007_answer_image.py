# Generated by Django 3.2.7 on 2021-09-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_remove_answer_answer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/answers/'),
        ),
    ]
