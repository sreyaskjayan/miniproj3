# Generated by Django 5.1.1 on 2024-11-04 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_photo', models.ImageField(upload_to='staff_photos/')),
                ('id_proof', models.ImageField(upload_to='staff_id_proofs/')),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit phone number', regex='^\\d{10}$')])),
                ('address', models.TextField()),
                ('location', models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50)),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(6)])),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
            ],
        ),
    ]
