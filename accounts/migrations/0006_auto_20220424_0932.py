# Generated by Django 3.2.5 on 2022-04-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220422_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='amount',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='typeofpos',
            new_name='type',
        ),
    ]