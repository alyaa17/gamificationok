# Generated by Django 4.1.5 on 2023-03-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='test_1',
            field=models.BooleanField(default=False),
        ),
    ]
