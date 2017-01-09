# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treenode',
            name='left_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_left_child', to='my_profile.TreeNode'),
        ),
        migrations.AlterField(
            model_name='treenode',
            name='right_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_right_child', to='my_profile.TreeNode'),
        ),
    ]
