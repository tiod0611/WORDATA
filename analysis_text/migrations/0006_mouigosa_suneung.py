# Generated by Django 2.2.3 on 2019-10-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_text', '0005_auto_20191019_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='mouigosa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbering', models.IntegerField(default=0)),
                ('word', models.CharField(max_length=50)),
                ('part_of_speech', models.CharField(max_length=20)),
                ('meaning', models.CharField(max_length=40)),
                ('example_sentence', models.TextField(blank=True, null=True)),
                ('sentence_interpretation', models.TextField(blank=True, null=True)),
                ('word_of_frequency', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='suneung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbering', models.IntegerField(default=0)),
                ('word', models.CharField(max_length=50)),
                ('part_of_speech', models.CharField(max_length=20)),
                ('meaning', models.CharField(max_length=40)),
                ('example_sentence', models.TextField(blank=True, null=True)),
                ('sentence_interpretation', models.TextField(blank=True, null=True)),
                ('word_of_frequency', models.IntegerField(default=0)),
            ],
        ),
    ]
