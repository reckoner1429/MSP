# Generated by Django 2.2.4 on 2019-09-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190910_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_ac',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_hod',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_professor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_ac',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_hod',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_professor',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_student',
        ),
        migrations.AddField(
            model_name='student',
            name='type_of_user',
            field=models.CharField(choices=[('Student', '0'), ('HOD', '1'), ('AC', '2'), ('Professor', '3')], default='3', max_length=1),
        ),
        migrations.AddField(
            model_name='teacher',
            name='type_of_user',
            field=models.CharField(choices=[('Student', '0'), ('HOD', '1'), ('AC', '2'), ('Professor', '3')], default='3', max_length=1),
        ),
    ]
