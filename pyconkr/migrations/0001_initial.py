# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'pyconkr_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pyconkr', ['Room'])

        # Adding model 'ProgramDate'
        db.create_table(u'pyconkr_programdate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'pyconkr', ['ProgramDate'])

        # Adding model 'ProgramTime'
        db.create_table(u'pyconkr_programtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'pyconkr', ['ProgramTime'])

        # Adding model 'SponsorLevel'
        db.create_table(u'pyconkr_sponsorlevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pyconkr', ['SponsorLevel'])

        # Adding model 'Sponsor'
        db.create_table(u'pyconkr_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pyconkr', ['Sponsor'])

        # Adding model 'Speaker'
        db.create_table(u'pyconkr_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'pyconkr', ['Speaker'])

        # Adding model 'Program'
        db.create_table(u'pyconkr_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slide_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyconkr.Room'])),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyconkr.ProgramDate'])),
        ))
        db.send_create_signal(u'pyconkr', ['Program'])

        # Adding M2M table for field speakers on 'Program'
        m2m_table_name = db.shorten_name(u'pyconkr_program_speakers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm[u'pyconkr.program'], null=False)),
            ('speaker', models.ForeignKey(orm[u'pyconkr.speaker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'speaker_id'])

        # Adding M2M table for field times on 'Program'
        m2m_table_name = db.shorten_name(u'pyconkr_program_times')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm[u'pyconkr.program'], null=False)),
            ('programtime', models.ForeignKey(orm[u'pyconkr.programtime'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'programtime_id'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'pyconkr_room')

        # Deleting model 'ProgramDate'
        db.delete_table(u'pyconkr_programdate')

        # Deleting model 'ProgramTime'
        db.delete_table(u'pyconkr_programtime')

        # Deleting model 'SponsorLevel'
        db.delete_table(u'pyconkr_sponsorlevel')

        # Deleting model 'Sponsor'
        db.delete_table(u'pyconkr_sponsor')

        # Deleting model 'Speaker'
        db.delete_table(u'pyconkr_speaker')

        # Deleting model 'Program'
        db.delete_table(u'pyconkr_program')

        # Removing M2M table for field speakers on 'Program'
        db.delete_table(db.shorten_name(u'pyconkr_program_speakers'))

        # Removing M2M table for field times on 'Program'
        db.delete_table(db.shorten_name(u'pyconkr_program_times'))


    models = {
        u'pyconkr.program': {
            'Meta': {'object_name': 'Program'},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyconkr.ProgramDate']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyconkr.Room']"}),
            'slide_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pyconkr.Speaker']", 'symmetrical': 'False', 'blank': 'True'}),
            'times': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pyconkr.ProgramTime']", 'symmetrical': 'False'})
        },
        u'pyconkr.programdate': {
            'Meta': {'object_name': 'ProgramDate'},
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyconkr.programtime': {
            'Meta': {'object_name': 'ProgramTime'},
            'begin': ('django.db.models.fields.TimeField', [], {}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyconkr.room': {
            'Meta': {'object_name': 'Room'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pyconkr.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'info': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'pyconkr.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'pyconkr.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['pyconkr']