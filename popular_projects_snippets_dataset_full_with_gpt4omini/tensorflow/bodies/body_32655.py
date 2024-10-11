# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
self.assertEqual((2, 2), linalg_ops.eye(num_rows=2).shape)
self.assertEqual((2, 3), linalg_ops.eye(num_rows=2, num_columns=3).shape)
