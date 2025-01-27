# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_file(
    key='aaa', vocabulary_file=self._unicode_vocabulary_file_name)
self.assertEqual('aaa', column.name)
self.assertEqual('aaa', column.key)
if isinstance(column.num_buckets, (int, np.integer)):
    self.assertEqual(165, column.num_buckets)
else:
    self.assertEqual(165, self.evaluate(column.num_buckets))
self.assertEqual({'aaa': parsing_ops.VarLenFeature(dtypes.string)},
                 column.parse_example_spec)
self.assertTrue(column._is_v2_column)
