# Generated by Django 4.2.1 on 2023-06-09 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0006_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='text',
            field=models.TextField(help_text='can use markdown'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_gain', models.PositiveSmallIntegerField()),
                ('pass_date', models.DateTimeField(auto_now=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_result', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Results',
                'ordering': ['user'],
            },
        ),
    ]
