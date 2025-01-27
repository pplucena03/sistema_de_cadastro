# Generated by Django 5.0.7 on 2024-07-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.TextField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
