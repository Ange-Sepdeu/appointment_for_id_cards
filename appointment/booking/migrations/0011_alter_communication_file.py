# Generated by Django 5.0.6 on 2024-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_communication_alter_document_birth_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static/communication/'),
        ),
    ]
