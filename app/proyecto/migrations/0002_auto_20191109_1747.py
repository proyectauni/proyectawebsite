# Generated by Django 2.2 on 2019-11-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='documentos',
            new_name='documento',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='proyecto/logo'),
        ),
    ]
