# Generated by Django 4.2.11 on 2024-04-07 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название компании')),
                ('description', models.TextField(default=0, verbose_name='описание компании')),
                ('city', models.CharField(max_length=250, verbose_name='город')),
                ('address', models.TextField(default=0, verbose_name='адресс компании')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название вакансии')),
                ('description', models.TextField(default=0, verbose_name='описание вакансии')),
                ('salary', models.FloatField(default=0, verbose_name='зарплата')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.company')),
            ],
        ),
    ]