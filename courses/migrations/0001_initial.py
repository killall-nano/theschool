# Generated by Django 2.2.24 on 2021-07-08 19:33

import courses.models
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
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=courses.models.save_subject_image, verbose_name='Subject Image')),
                ('description', models.TextField(blank=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter no. ')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=courses.models.save_lesson_files, verbose_name='Video')),
                ('ppt', models.FileField(blank=True, null=True, upload_to=courses.models.save_lesson_files, verbose_name='Presentation')),
                ('Notes', models.FileField(blank=True, null=True, upload_to=courses.models.save_lesson_files, verbose_name='Notes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Subject')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
