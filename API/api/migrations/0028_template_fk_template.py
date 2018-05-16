# Generated by Django 2.0.5 on 2018-05-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_remove_name_fk_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='fk_template',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='api.Name'),
            preserve_default=False,
        ),
    ]