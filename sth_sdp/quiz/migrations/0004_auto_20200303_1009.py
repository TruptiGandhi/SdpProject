# Generated by Django 2.2.7 on 2020-03-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200303_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitting',
            name='q_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='question type'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='question type'),
        ),
    ]
