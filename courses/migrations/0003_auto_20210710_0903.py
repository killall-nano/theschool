# Generated by Django 2.2.24 on 2021-07-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lesson_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.Lesson'),
        ),
    ]
