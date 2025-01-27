# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
batch_shape = (2, 3)
self.assertEqual(
    (2, 3, 2, 2),
    linalg_ops.eye(num_rows=2, batch_shape=batch_shape).shape)
self.assertEqual(
    (2, 3, 2, 3),
    linalg_ops.eye(
        num_rows=2, num_columns=3, batch_shape=batch_shape).shape)
