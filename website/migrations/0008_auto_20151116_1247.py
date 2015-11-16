# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20151116_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name=b'Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'First Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='github_link',
            field=models.SlugField(max_length=100, null=True, verbose_name=b'GitHub account', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Last Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='payment_service',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'wepay', 'WePay')]),
            preserve_default=True,
        ),
    ]
