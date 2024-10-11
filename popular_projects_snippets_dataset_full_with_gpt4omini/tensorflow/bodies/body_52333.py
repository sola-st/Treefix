# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
a = sfc.sequence_numeric_column('aaa', shape=[1, 2])
self.assertEqual((1, 2), a.shape)
