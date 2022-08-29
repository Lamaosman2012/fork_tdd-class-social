# Generated by Django 4.0.6 on 2022-08-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('website', models.URLField(blank=True, max_length=300, null=True)),
                ('about', models.TextField(blank=True, max_length=1000, null=True)),
                ('role', models.CharField(choices=[('STD', 'Student'), ('INS', 'Institution'), ('TEC', 'Teacher'), ('OTH', 'Others')], default='Others', max_length=3)),
                ('connections', models.ManyToManyField(blank=True, related_name='users', to='user_mgmt.baseuser')),
            ],
        ),
    ]
