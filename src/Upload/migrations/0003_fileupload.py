# Generated by Django 3.2.7 on 2021-10-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0002_alter_upload_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('when_uploaded', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
