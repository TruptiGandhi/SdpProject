# Generated by Django 2.2.7 on 2020-03-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200316_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='q_time',
            field=models.IntegerField(blank=True, default=True, null=True, verbose_name='question time'),
        ),
    ]
