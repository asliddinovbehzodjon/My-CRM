# Generated by Django 4.1.5 on 2023-02-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_davomat_options_alter_davomat_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_kodi', models.CharField(max_length=100)),
                ('fan_nomi', models.CharField(max_length=100)),
                ('talaba', models.CharField(max_length=100)),
                ('telefon_raqam', models.CharField(max_length=100)),
                ('savollar_soni', models.CharField(max_length=100)),
                ('togri_javoblar', models.CharField(max_length=100)),
            ],
        ),
    ]