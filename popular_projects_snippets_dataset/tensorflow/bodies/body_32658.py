# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
eye_np = np.eye(num_rows, M=num_columns, dtype=dtype.as_numpy_dtype)
if batch_shape is not None:
    eye_np = np.tile(eye_np, batch_shape + [1, 1])
eye_tf = self.evaluate(linalg_ops.eye(
    num_rows,
    num_columns=num_columns,
    batch_shape=batch_shape,
    dtype=dtype))
self.assertAllEqual(eye_np, eye_tf)
