# Generated by Django 3.2.5 on 2021-07-19 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_days', to='courses.standard')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_time_slots', to='courses.standard')),
            ],
        ),
        migrations.CreateModel(
            name='SlotSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_days', to='courses.workingdays')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_time', to='courses.timeslots')),
                ('slot_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_subject', to='courses.subject')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots', to='courses.standard')),
            ],
        ),
    ]