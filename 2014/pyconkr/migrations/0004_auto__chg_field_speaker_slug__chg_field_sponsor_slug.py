# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Speaker.slug'
        db.alter_column(u'pyconkr_speaker', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100))

        # Changing field 'Sponsor.slug'
        db.alter_column(u'pyconkr_sponsor', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Speaker.slug'
        db.alter_column(u'pyconkr_speaker', 'slug', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sponsor.slug'
        db.alter_column(u'pyconkr_sponsor', 'slug', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'pyconkr.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyconkr.SponsorLevel']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
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