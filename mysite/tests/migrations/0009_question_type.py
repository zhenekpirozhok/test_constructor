# Generated by Django 3.2.7 on 2021-09-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('M', 'Множественный'), ('S', 'Одинаочный')], default='S', max_length=1),
        ),
    ]