# Generated by Django 3.0.3 on 2020-03-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200326_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text1',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text2',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text3',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
