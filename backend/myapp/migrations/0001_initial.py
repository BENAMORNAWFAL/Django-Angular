# Generated by Django 4.2.6 on 2023-10-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.TextField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]