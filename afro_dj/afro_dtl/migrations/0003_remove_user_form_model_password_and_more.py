# Generated by Django 4.2 on 2023-04-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afro_dtl', '0002_user_form_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_form_model',
            name='password',
        ),
        migrations.AddField(
            model_name='user_form_model',
            name='message',
            field=models.TextField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
