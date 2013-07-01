# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Log.ip'
        db.add_column(u'webpassapp_log', 'ip',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Log.ip'
        db.delete_column(u'webpassapp_log', 'ip')


    models = {
        u'webpassapp.counter': {
            'Meta': {'object_name': 'Counter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_counter': ('django.db.models.fields.IntegerField', [], {})
        },
        u'webpassapp.log': {
            'Meta': {'ordering': "['-date_pub']", 'object_name': 'Log'},
            'brauser': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['webpassapp']