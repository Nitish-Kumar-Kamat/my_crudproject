# Generated by Django 4.0.5 on 2023-07-29 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
