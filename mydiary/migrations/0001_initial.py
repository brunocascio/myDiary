# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiaryComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiaryVote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthdate', models.DateField(null=True)),
                ('friends', models.ManyToManyField(through='mydiary.Friendship', to='mydiary.UserProfile')),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': "User's profiles",
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user1',
            field=models.ForeignKey(related_name='relation_source', to='mydiary.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friendship',
            name='user2',
            field=models.ForeignKey(related_name='relation_target', to='mydiary.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('user1', 'user2')]),
        ),
        migrations.AddField(
            model_name='diaryvote',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diaryvote',
            name='diary',
            field=models.ForeignKey(to='mydiary.Diary'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diarycomment',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diarycomment',
            name='diary',
            field=models.ForeignKey(to='mydiary.Diary'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diary',
            name='tags',
            field=models.ManyToManyField(to='mydiary.Tag'),
            preserve_default=True,
        ),
    ]
