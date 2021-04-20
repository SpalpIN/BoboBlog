# Generated by Django 3.2 on 2021-04-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='publish',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='created'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
