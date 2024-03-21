# Generated by Django 4.2.7 on 2024-03-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.AddField(
            model_name='contact',
            name='e_mail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Логин'),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]