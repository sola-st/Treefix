# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
num_rows = num_rows_fn()
num_columns = num_columns_fn()
batch_shape = (2, 3)
identity_matrix = linalg_ops.eye(
    num_rows=num_rows,
    num_columns=num_columns,
    batch_shape=batch_shape)
self.assertEqual(4, identity_matrix.shape.ndims)
self.assertEqual((2, 3), identity_matrix.shape[:2])
if num_rows is not None and not isinstance(num_rows, ops.Tensor):
    self.assertEqual(2, identity_matrix.shape[-2])

if num_columns is not None and not isinstance(num_columns, ops.Tensor):
    self.assertEqual(3, identity_matrix.shape[-1])
