# Generated by Django 4.1.1 on 2022-10-20 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escribir',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('write_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='asdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_text', models.CharField(max_length=200)),
                ('fkid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.escribir')),
            ],
        ),
    ]
