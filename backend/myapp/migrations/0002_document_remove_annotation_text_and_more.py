# Generated by Django 4.1.12 on 2023-11-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='text',
        ),
        migrations.AlterField(
            model_name='annotation',
            name='label',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.document'),
        ),
    ]
