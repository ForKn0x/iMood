# Generated by Django 3.2.7 on 2022-01-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0002_auto_20220116_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='feelings_tags',
            field=models.ManyToManyField(to='mood.FeelingsTag'),
        ),
    ]
