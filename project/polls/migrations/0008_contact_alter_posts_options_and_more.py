# Generated by Django 4.0.2 on 2022-05-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_categories_describe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('msgdate', models.DateField(null=True)),
                ('isread', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['title', 'slug'], 'verbose_name': 'AnimePosts', 'verbose_name_plural': 'AnimePosts'},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['name', 'lastname'], 'verbose_name': 'Regis', 'verbose_name_plural': 'Registration'},
        ),
    ]
