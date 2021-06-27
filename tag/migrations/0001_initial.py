# Generated by Django 3.2.4 on 2021-06-13 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QASample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_document', models.TextField(blank=True, null=True)),
                ('positive_document_title', models.CharField(blank=True, max_length=300, null=True)),
                ('question', models.CharField(blank=True, max_length=300, null=True)),
                ('hard_negative_document', models.TextField(blank=True, null=True)),
                ('hard_negative_document_title', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.qasample')),
            ],
        ),
    ]
