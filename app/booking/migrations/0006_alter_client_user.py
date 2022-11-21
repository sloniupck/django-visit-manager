# Generated by Django 4.0 on 2022-11-12 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('booking', '0005_visit_time_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='auth.user'),
        ),
    ]
