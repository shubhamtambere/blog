# Generated by Django 2.0.7 on 2019-01-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(default=-1, primary_key=True, serialize=False),
        ),
    ]
