# Generated by Django 3.2.7 on 2021-09-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_answer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/answers/'),
        ),
    ]
