# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# These should be sorted lexicographically based on their string
# representations. For FeatureColumns, this looks like
# '<__main__.FeatureColumn object at ...>'.

a = fc.numeric_column('first')  # '<__main__.NumericColumn ...>'
b = fc.numeric_column('second')  # '<__main__.NumericColumn ...>'
c = fc_old._numeric_column('third')  # '<__main__._NumericColumn ...>'

sorted_sequence = ['0', a, b, c, 'd']
reversed_sequence = sorted_sequence[::-1]
self.assertAllEqual(sorted(reversed_sequence), sorted_sequence)

# pylint: disable=g-generic-assert
self.assertTrue(a < b)  # V2 < V2 feature columns.
self.assertTrue(a < c)  # V2 < V1 feature columns.
self.assertFalse(c < a)  # V1 < V2 feature columns.
self.assertTrue('0' < a)  # string < V2 feature column.
self.assertTrue(a < 'd')  # V2 feature column < string.
