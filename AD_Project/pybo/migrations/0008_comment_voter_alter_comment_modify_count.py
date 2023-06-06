# Generated by Django 4.2 on 2023-06-01 11:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0007_answer_modify_count_comment_modify_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='voter',
            field=models.ManyToManyField(related_name='voter_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
