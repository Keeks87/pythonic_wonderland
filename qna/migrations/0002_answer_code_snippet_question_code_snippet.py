# Generated by Django 5.0 on 2023-12-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='code_snippet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='code_snippet',
            field=models.TextField(blank=True, null=True),
        ),
    ]
