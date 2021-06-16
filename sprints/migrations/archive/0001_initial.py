<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-06-16 13:37
=======
# Generated by Django 3.2.4 on 2021-06-16 13:07
>>>>>>> development

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_sprints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyIntention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_intention', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weekly_intentions', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='SprintHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('habit_description', models.CharField(max_length=250)),
                ('is_done', models.BooleanField(default=False)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprint_habits', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='SprintGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('goal_description', models.CharField(max_length=250)),
                ('is_done', models.BooleanField(default=False)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprint_goals', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='DailyToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_item', models.CharField(blank=True, max_length=50, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_dos', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='DailyMood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moods', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='DailyGratitude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_gratitude', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='daily_gratitudes', to='sprints.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='DailyEnergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_level', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('sprint', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='energy_levels', to='sprints.sprint')),
            ],
        ),
    ]
