# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
x = x()
y = y()
for validate in (True, False):
    result = x._merge_precomputed_encodings(y, validate)
    self.assertEqual(result._has_precomputed_row_splits(),
                     'row_splits' in expected_encodings)
    self.assertEqual(result._has_precomputed_row_lengths(),
                     'row_lengths' in expected_encodings)
    self.assertEqual(result._has_precomputed_value_rowids(),
                     'value_rowids' in expected_encodings)
    self.assertEqual(result._has_precomputed_nrows(),
                     'nrows' in expected_encodings)
    self.assertEqual(result.uniform_row_length() is not None,
                     'uniform_row_length' in expected_encodings)
    for r in (x, y):
        if (r._has_precomputed_row_splits() and
            result._has_precomputed_row_splits()):
            self.assertAllEqual(r.row_splits(), result.row_splits())
        if (r._has_precomputed_row_lengths() and
            result._has_precomputed_row_lengths()):
            self.assertAllEqual(r.row_lengths(), result.row_lengths())
        if (r._has_precomputed_value_rowids() and
            result._has_precomputed_value_rowids()):
            self.assertAllEqual(r.value_rowids(), result.value_rowids())
        if r._has_precomputed_nrows() and result._has_precomputed_nrows():
            self.assertAllEqual(r.nrows(), result.nrows())
        if (r.uniform_row_length() is not None and
            result.uniform_row_length() is not None):
            self.assertAllEqual(r.uniform_row_length(),
                                result.uniform_row_length())
