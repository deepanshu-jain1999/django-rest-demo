# Generated by Django 2.0.1 on 2018-01-31 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('start_year', models.IntegerField(blank=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]