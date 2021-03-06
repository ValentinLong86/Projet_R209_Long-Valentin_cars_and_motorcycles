# Generated by Django 4.0.3 on 2022-05-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('cylinder', models.IntegerField()),
                ('release_date', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('horses', models.IntegerField()),
                ('release_date', models.IntegerField(blank=True)),
                ('marque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars_and_motorcycles.marque')),
            ],
        ),
    ]
