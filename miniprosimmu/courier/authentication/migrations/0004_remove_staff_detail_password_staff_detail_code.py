# Generated by Django 5.1.1 on 2024-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_staff_detail_delete_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_detail',
            name='password',
        ),
        migrations.AddField(
            model_name='staff_detail',
            name='code',
            field=models.CharField(default=1234, max_length=4),
            preserve_default=False,
        ),
    ]