# Generated by Django 2.2.3 on 2019-07-24 18:06

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
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.IntegerField(default=True)),
                ('people', models.IntegerField(default=True)),
                ('labels', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.IntegerField(default=True)),
                ('people', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Singers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=True)),
                ('nationality', models.CharField(max_length=50)),
                ('groups', models.CharField(max_length=50)),
                ('rate', models.FloatField(default=True)),
                ('comments', models.CharField(default=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solo_singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.IntegerField(default=True)),
                ('people', models.IntegerField(default=True)),
                ('labels', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_dislike', models.CharField(choices=[(0, 'like'), (1, 'dislike')], max_length=1)),
                ('comments', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]