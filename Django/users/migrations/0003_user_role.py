# Generated by Django 3.1.3 on 2020-11-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201124_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'User'), ('ROC', 'ROC'), ('ADMIN', 'Admin')], default='USER', max_length=20),
        ),
    ]