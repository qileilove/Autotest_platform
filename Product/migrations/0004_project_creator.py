# Generated by Django 2.1.7 on 2019-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_remove_project_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.IntegerField(default=1),
        ),
    ]