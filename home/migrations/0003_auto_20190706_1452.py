# Generated by Django 2.2 on 2019-07-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190706_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guides',
            name='contact',
            field=models.TextField(),
        ),
    ]
