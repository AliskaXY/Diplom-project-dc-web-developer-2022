# Generated by Django 4.2.3 on 2023-07-12 15:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('slug', models.CharField(default='', max_length=256)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('level', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)])),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2, verbose_name='Task status')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='TestingInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.CharField(default='', max_length=256)),
                ('expected_output', models.CharField(default=None, max_length=256, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='tasks.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_language', models.CharField(blank=True, choices=[('PY', 'Python'), ('JS', 'JavaScript'), ('HTML', 'HTML'), ('SQL', 'SQL'), ('PHP', 'PHP'), ('C', 'C'), ('CPP', 'C++')], default=None, max_length=4, verbose_name='Programming language')),
                ('test_file', models.FileField(blank=True, default=None, null=True, upload_to=tasks.models.tasks_tests_directory_path)),
                ('solution_file', models.FileField(blank=True, default=None, null=True, upload_to=tasks.models.tasks_solution_directory_path)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='tasks.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BooleanField(default=False)),
                ('exp_gain', models.PositiveSmallIntegerField(default=0)),
                ('prog_language', models.CharField(blank=True, choices=[('PY', 'Python'), ('JS', 'JavaScript'), ('HTML', 'HTML'), ('SQL', 'SQL'), ('PHP', 'PHP'), ('C', 'C'), ('CPP', 'C++')], default=None, max_length=4, verbose_name='Programming language')),
                ('result_code', models.FileField(blank=True, default=None, null=True, upload_to=tasks.models.user_tasks_result_directory_path)),
                ('result_message', models.FileField(blank=True, default=None, null=True, upload_to=tasks.models.user_tasks_result_directory_path)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='tasklanguage',
            constraint=models.UniqueConstraint(fields=('task', 'prog_language'), name='unique_language'),
        ),
    ]