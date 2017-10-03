# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('parameters_schema', jsonfield.fields.JSONField(default={b'$schema': b'http://json-schema.org/schema#', b'type': b'object', b'properties': {}})),
                ('author', models.ForeignKey(related_name='analysis', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'timeside_analysis',
                'verbose_name': 'Analysis',
                'verbose_name_plural': 'Analyses',
            },
        ),
        migrations.CreateModel(
            name='AnalysisTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('analysis', models.ForeignKey(related_name='tracks', verbose_name='analysis', to='server.Analysis')),
                ('author', models.ForeignKey(related_name='analysistrack', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'timeside_analysis_tracks',
                'verbose_name': 'Analysis Track',
            },
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('start_time', models.FloatField(default=0, verbose_name='start time (s)')),
                ('stop_time', models.FloatField(verbose_name='stop time (s)')),
                ('author', models.ForeignKey(related_name='annotation', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnotationTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('overlapping', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='annotationtrack', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'timeside_annotation_tracks',
                'verbose_name': 'Annotation Track',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(related_name='experience', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('experiences', models.ManyToManyField(related_name='other_experiences', verbose_name='other experiences', to='server.Experience', blank=True)),
            ],
            options={
                'db_table': 'timeside_experiences',
                'verbose_name': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('source_file', models.FileField(upload_to=b'items/%Y/%m/%d', max_length=1024, verbose_name='file', blank=True)),
                ('source_url', models.URLField(max_length=1024, verbose_name='URL', blank=True)),
                ('audio_duration', models.FloatField(null=True, verbose_name='duration', blank=True)),
                ('sha1', models.CharField(max_length=512, verbose_name='sha1', blank=True)),
                ('mime_type', models.CharField(max_length=256, verbose_name='mime type', blank=True)),
                ('hdf5', models.FileField(upload_to=b'results/%Y/%m/%d', max_length=1024, verbose_name='HDF5 result file', blank=True)),
                ('lock', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='item', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'timeside_items',
                'verbose_name': 'item',
            },
        ),
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('parameters', models.TextField(default=b'{}', verbose_name='Parameters', blank=True)),
                ('author', models.ForeignKey(related_name='preset', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'timeside_presets',
                'verbose_name': 'Preset',
                'verbose_name_plural': 'Presets',
            },
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.CharField(unique=True, max_length=128, verbose_name='pid')),
                ('version', models.CharField(max_length=64, verbose_name='version', blank=True)),
                ('name', models.CharField(max_length=256, verbose_name='name', blank=True)),
            ],
            options={
                'db_table': 'timeside_processors',
                'verbose_name': 'processor',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('hdf5', models.FileField(upload_to=b'results/%Y/%m/%d', max_length=1024, verbose_name='HDF5 result file', blank=True)),
                ('file', models.FileField(upload_to=b'results/%Y/%m/%d', max_length=1024, verbose_name='Output file', blank=True)),
                ('mime_type', models.CharField(max_length=256, verbose_name='Output file MIME type', blank=True)),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'failed'), (1, 'draft'), (2, 'pending'), (3, 'running'), (4, 'done')])),
                ('author', models.ForeignKey(related_name='result', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('item', models.ForeignKey(related_name='results', on_delete=django.db.models.deletion.SET_NULL, verbose_name='item', blank=True, to='server.Item', null=True)),
                ('preset', models.ForeignKey(related_name='results', on_delete=django.db.models.deletion.SET_NULL, verbose_name='preset', blank=True, to='server.Preset', null=True)),
            ],
            options={
                'db_table': 'timeside_results',
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='title', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(related_name='selection', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('items', models.ManyToManyField(related_name='selections', verbose_name='items', to='server.Item', blank=True)),
                ('selections', models.ManyToManyField(related_name='other_selections', verbose_name='other selections', to='server.Selection', blank=True)),
            ],
            options={
                'db_table': 'timeside_selections',
                'verbose_name': 'selection',
            },
        ),
        migrations.CreateModel(
            name='SubProcessor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_processor_id', models.CharField(unique=True, max_length=128, verbose_name='sub_processor_id')),
                ('name', models.CharField(max_length=256, verbose_name='name', blank=True)),
                ('processor', models.ForeignKey(related_name='sub_results', verbose_name='processor', blank=True, to='server.Processor', null=True)),
            ],
            options={
                'db_table': 'timeside_subprocessors',
                'verbose_name': 'Subprocessor',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added', null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified', null=True)),
                ('uuid', models.CharField(verbose_name='uuid', unique=True, max_length=255, editable=False, blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'failed'), (1, 'draft'), (2, 'pending'), (3, 'running'), (4, 'done')])),
                ('author', models.ForeignKey(related_name='task', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('experience', models.ForeignKey(related_name='task', verbose_name='experience', blank=True, to='server.Experience', null=True)),
                ('selection', models.ForeignKey(related_name='task', verbose_name='selection', blank=True, to='server.Selection', null=True)),
            ],
            options={
                'db_table': 'timeside_tasks',
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AddField(
            model_name='preset',
            name='processor',
            field=models.ForeignKey(related_name='presets', verbose_name='processor', blank=True, to='server.Processor', null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='presets',
            field=models.ManyToManyField(related_name='experiences', verbose_name='presets', to='server.Preset', blank=True),
        ),
        migrations.AddField(
            model_name='annotationtrack',
            name='item',
            field=models.ForeignKey(related_name='annotation_tracks', verbose_name='item', to='server.Item'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='track',
            field=models.ForeignKey(related_name='annotations', verbose_name='annotation', to='server.AnnotationTrack'),
        ),
        migrations.AddField(
            model_name='analysistrack',
            name='item',
            field=models.ForeignKey(related_name='analysis_tracks', verbose_name='item', to='server.Item'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='preset',
            field=models.ForeignKey(related_name='analysis', verbose_name='preset', to='server.Preset'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='sub_processor',
            field=models.ForeignKey(related_name='analysis', verbose_name='sub_processor', to='server.SubProcessor'),
        ),
    ]
