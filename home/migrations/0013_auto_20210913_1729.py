# Generated by Django 3.2.7 on 2021-09-13 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_faq_myfaq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_verification',
            old_name='last_modified_time',
            new_name='last_updated_at',
        ),
        migrations.RenameField(
            model_name='myfaq',
            old_name='last_modified_time',
            new_name='last_updated_at',
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='last_modified_time',
            new_name='last_updated_at',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='last_modified_time',
            new_name='last_updated_at',
        ),
        migrations.RenameField(
            model_name='userproblemdata',
            old_name='last_modified_time',
            new_name='last_updated_at',
        ),
        migrations.RemoveField(
            model_name='account_verification',
            name='last_modified_data',
        ),
        migrations.RemoveField(
            model_name='myfaq',
            name='last_modified_data',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='last_modified_data',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='last_modified_data',
        ),
        migrations.RemoveField(
            model_name='userproblemdata',
            name='last_modified_data',
        ),
        migrations.AddField(
            model_name='account_verification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myfaq',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userproblemdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_url',
            field=models.URLField(max_length=250),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solution_url',
            field=models.URLField(max_length=250),
        ),
        migrations.AlterField(
            model_name='problem',
            name='video_url',
            field=models.CharField(blank=True, default='#', max_length=250, null=True),
        ),
    ]
