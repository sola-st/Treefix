# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests that the name does not depend on the order of given columns."""
a = fc._numeric_column('a', dtype=dtypes.int32)
b = fc._bucketized_column(a, boundaries=[0, 1])
crossed1 = fc._crossed_column(['d1', 'd2'], 10)

crossed2 = fc._crossed_column([crossed1, 'c', b], 10)
self.assertEqual('a_bucketized_X_c_X_d1_X_d2', crossed2.name)
