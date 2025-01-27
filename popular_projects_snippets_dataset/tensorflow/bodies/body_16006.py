# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = rp_factory()
self.assertEqual(rp._has_precomputed_row_splits(),
                 'row_splits' in expected_encodings)
self.assertEqual(rp._has_precomputed_row_lengths(),
                 'row_lengths' in expected_encodings)
self.assertEqual(rp._has_precomputed_value_rowids(),
                 'value_rowids' in expected_encodings)
self.assertEqual(rp._has_precomputed_nrows(), 'nrows' in expected_encodings)
