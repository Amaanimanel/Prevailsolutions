# Generated by Django 3.2.5 on 2022-04-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_investor_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
