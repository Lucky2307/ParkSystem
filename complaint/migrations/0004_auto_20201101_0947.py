# Generated by Django 3.1.2 on 2020-11-01 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('complaint', '0003_auto_20201101_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintmessage',
            name='member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member'),
        ),
    ]
