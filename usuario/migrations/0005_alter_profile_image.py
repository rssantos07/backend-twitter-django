# Generated by Django 5.0.6 on 2024-06-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0004_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="user_images/"
            ),
        ),
    ]
