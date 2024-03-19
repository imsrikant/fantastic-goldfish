# Generated by Django 4.2.11 on 2024-03-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_orphanage_skill_alter_user_email_userskill_problem_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="user",
            name="contact_number",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="user_id",
            field=models.AutoField(
                default="Volunteer", primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("volunteer", "Volunteer"), ("ngo", "NGO")],
                default="Volunteer",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128),
        ),
    ]
