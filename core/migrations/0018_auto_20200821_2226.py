# Generated by Django 3.0.8 on 2020-08-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_newsfeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('EMERGENCY', 'Emergency'), ('OFFICE', 'Office'), ('FACULTY_STAFF', 'Faculty/Staff'), ('OTHER', 'Other')], max_length=13),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='platforms',
            field=models.CharField(choices=[('TEXT_CALL', 'Text/Call'), ('WHATSAPP', 'Text/WhatsApp/Call')], default='TEXT/CALL', max_length=9, null=True),
        ),
    ]
