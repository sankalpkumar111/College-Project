# Generated by Django 5.0.4 on 2024-05-03 07:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduLink', '0003_subject_sessions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student'), (4, 'Accountant')], default=1, max_length=1),
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fee_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduLink.feecategory')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduLink.student')),
            ],
        ),
        migrations.CreateModel(
            name='FeeReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('reminder_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fee_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduLink.feecategory')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduLink.student')),
            ],
        ),
    ]
