# Generated by Django 3.2.4 on 2021-06-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyenergy',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dailygratitude',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dailymood',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dailytodo',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sprintgoal',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sprinthabit',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='weeklyintention',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]