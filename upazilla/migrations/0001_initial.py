# Generated by Django 2.2.12 on 2021-12-08 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0002_auto_20211208_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Model')),
            ],
        ),
    ]
