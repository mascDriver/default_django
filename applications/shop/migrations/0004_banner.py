# Generated by Django 2.2.12 on 2020-04-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0003_auto_20200421_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Texto em destaque do banner')),
                ('banner', models.ImageField(upload_to='media/')),
                ('texto', models.TextField()),
                ('ativo', models.BooleanField(default=False, verbose_name='O banner esta ativo?')),
            ],
        ),
    ]
