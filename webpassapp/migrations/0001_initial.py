# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table('webpassapp_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('brauser', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('webpassapp', ['Log'])

        # Adding model 'Counter'
        db.create_table('webpassapp_counter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pass_counter', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('webpassapp', ['Counter'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table('webpassapp_log')

        # Deleting model 'Counter'
        db.delete_table('webpassapp_counter')


    models = {
        'webpassapp.counter': {
            'Meta': {'object_name': 'Counter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_counter': ('django.db.models.fields.IntegerField', [], {})
        },
        'webpassapp.log': {
            'Meta': {'ordering': "['-date_pub']", 'object_name': 'Log'},
            'brauser': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['webpassapp']