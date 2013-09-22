# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'cashregister_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('auth_type', self.gf('django.db.models.fields.IntegerField')()),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cashregister', ['User'])

        # Adding model 'ProductCategory'
        db.create_table(u'cashregister_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'cashregister', ['ProductCategory'])

        # Adding model 'Product'
        db.create_table(u'cashregister_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.ProductCategory'])),
            ('stock', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gross_unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('mva_rate', self.gf('django.db.models.fields.IntegerField')(default=15)),
        ))
        db.send_create_signal(u'cashregister', ['Product'])

        # Adding model 'SalesTransaction'
        db.create_table(u'cashregister_salestransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('reversal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.User'])),
            ('net_total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('total_mva', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('gross_total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'cashregister', ['SalesTransaction'])

        # Adding model 'SalesTransactionItem'
        db.create_table(u'cashregister_salestransactionitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salestransaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.SalesTransaction'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.Product'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('net_unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('unit_mva', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'cashregister', ['SalesTransactionItem'])

        # Adding model 'Restocking'
        db.create_table(u'cashregister_restocking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('deficit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.User'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cashregister.Product'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('net_unit_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'cashregister', ['Restocking'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'cashregister_user')

        # Deleting model 'ProductCategory'
        db.delete_table(u'cashregister_productcategory')

        # Deleting model 'Product'
        db.delete_table(u'cashregister_product')

        # Deleting model 'SalesTransaction'
        db.delete_table(u'cashregister_salestransaction')

        # Deleting model 'SalesTransactionItem'
        db.delete_table(u'cashregister_salestransactionitem')

        # Deleting model 'Restocking'
        db.delete_table(u'cashregister_restocking')


    models = {
        u'cashregister.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.ProductCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gross_unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mva_rate': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'stock': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'cashregister.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'cashregister.restocking': {
            'Meta': {'object_name': 'Restocking'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'deficit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_unit_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.Product']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.User']"})
        },
        u'cashregister.salestransaction': {
            'Meta': {'object_name': 'SalesTransaction'},
            'gross_total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'reversal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'total_mva': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.User']"})
        },
        u'cashregister.salestransactionitem': {
            'Meta': {'object_name': 'SalesTransactionItem'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.Product']"}),
            'salestransaction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.SalesTransaction']"}),
            'unit_mva': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'cashregister.user': {
            'Meta': {'object_name': 'User'},
            'auth_type': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['cashregister']