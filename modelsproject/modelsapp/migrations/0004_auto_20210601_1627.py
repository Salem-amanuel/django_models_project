# Generated by Django 3.2.3 on 2021-06-01 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0003_certificate_type_department_faculty_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate_type',
            old_name='name',
            new_name='Certificate_type',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='name',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='year_of_graduation',
        ),
        migrations.RemoveField(
            model_name='school',
            name='address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_resumption',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='Certificate_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsapp.certificate_type'),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsapp.grade'),
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsapp.faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsapp.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsapp.school'),
        ),
    ]
