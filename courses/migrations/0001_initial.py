# Generated by Django 4.1.5 on 2023-01-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Course name')),
                ('cost', models.CharField(max_length=100, verbose_name='Course price')),
            ],
            options={
                'verbose_name': 'Course ',
                'verbose_name_plural': 'Courses ',
            },
        ),
    ]