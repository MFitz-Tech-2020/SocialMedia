# Generated by Django 2.2.9 on 2020-02-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200215_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdetailpage',
            name='summary',
            field=models.TextField(default='Input the summary...', help_text='Overwrites the default title'),
        ),
    ]
