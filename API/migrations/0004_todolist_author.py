# Generated by Django 4.2 on 2025-01-01 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.user', verbose_name='Author'),
        ),
    ]