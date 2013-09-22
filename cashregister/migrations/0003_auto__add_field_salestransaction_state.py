# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SalesTransaction.state'
        db.add_column(u'cashregister_salestransaction', 'state',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SalesTransaction.state'
        db.delete_column(u'cashregister_salestransaction', 'state')


    models = {
        u'cashregister.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashregister.ProductCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'total_mva': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
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