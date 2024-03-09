# Generated by Django 5.0.3 on 2024-03-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_githubmodel_email_githubmodel_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubmodel',
            name='bio',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Bio do usuário'),
        ),
        migrations.AlterField(
            model_name='githubmodel',
            name='login',
            field=models.CharField(max_length=25, verbose_name='Nome do usuário'),
        ),
    ]