# Generated by Django 5.0.3 on 2024-03-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_service_team_alter_aboutus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
