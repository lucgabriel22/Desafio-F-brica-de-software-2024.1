# Generated by Django 5.0.3 on 2024-03-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_githubmodel_bio_alter_githubmodel_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubmodel',
            name='bio',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Bio do usuário'),
        ),
    ]
