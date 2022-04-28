# Generated by Django 3.2.5 on 2022-04-21 17:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('category', models.CharField(choices=[('Idea-phase', 'Idea-phase'), ('Semi-completed', 'Semi-completed'), ('Fully-completed', 'Fully-completed')], max_length=200, null=True)),
                ('descripton', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('State', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('industry', models.CharField(max_length=200, null=True)),
                ('typeofpos', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Temporal', 'Temporal'), ('Permanent', 'Permanent'), ('contract', 'contract')], default='Full-time', max_length=200, null=True)),
                ('Shift', models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening'), ('Night', 'Night')], default='Day', max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(900000)])),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('investor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.investor')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]