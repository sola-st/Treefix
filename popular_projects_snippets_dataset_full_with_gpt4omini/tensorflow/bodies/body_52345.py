# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests parents attribute of column."""
column = sfc.sequence_numeric_column(key='my-key')
self.assertEqual(column.parents, ['my-key'])
