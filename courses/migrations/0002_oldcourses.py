# Generated by Django 2.1.5 on 2019-02-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Old course')),
                ('description', models.TextField(default='This is a description of the old course...')),
                ('price', models.TextField(default='99.99')),
            ],
        ),
    ]
