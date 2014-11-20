# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0002_friendship_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.ForeignKey(to='mydiary.Diary', null=True)),
                ('emitter', models.ForeignKey(to='mydiary.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notification', models.ForeignKey(to='mydiary.Notification')),
                ('receptor', models.ForeignKey(to='mydiary.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='usernotification',
            unique_together=set([('receptor', 'notification')]),
        ),
        migrations.AddField(
            model_name='notification',
            name='type_notification',
            field=models.ForeignKey(to='mydiary.TypeNotification'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notifications',
            field=models.ManyToManyField(related_name='user_notifications', through='mydiary.UserNotification', to='mydiary.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='user_friends', through='mydiary.Friendship', to='mydiary.UserProfile'),
            preserve_default=True,
        ),
    ]
