# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
self.assertEqual(a.nrows, b.nrows, msg)
self.assertEqual(a.nvals, b.nvals, msg)
self.assertEqual(a.uniform_row_length, b.uniform_row_length, msg)
self.assertEqual(a.dtype, b.dtype, msg)
