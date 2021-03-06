# Generated by Django 4.0.4 on 2022-04-23 11:42

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
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('calorie', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('trans_fat', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('sodium', models.FloatField()),
                ('sugar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food_control.food')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
