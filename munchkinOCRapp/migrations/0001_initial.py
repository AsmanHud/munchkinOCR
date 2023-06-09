# Generated by Django 4.2.2 on 2023-06-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hirelings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('bonus', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('level', models.IntegerField()),
                ('bad_stuff', models.TextField()),
                ('is_two_levels', models.BooleanField(default=False)),
                ('treasures', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonsterModifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('modifier', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Steeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=200, unique=True)),
                ('name_ru', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('bonus', models.IntegerField()),
                ('is_big', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
