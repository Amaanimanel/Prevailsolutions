# Generated by Django 3.2.5 on 2022-04-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220424_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='resume',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='uploads/'),
        ),
    ]
