# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
self._testSparseDenseInvalidInputs(
    a_indices=constant_op.constant(0, shape=[17, 2], dtype=dtypes.int64),
    a_values=constant_op.constant(0, shape=[5], dtype=dtypes.float32),
    a_shape=constant_op.constant([3, 4], dtype=dtypes.int64),
    b=constant_op.constant(1, shape=[3, 4], dtype=dtypes.float32),
    expected_error="Dimensions 17 and 5 are not compatible")
self._testSparseDenseInvalidInputs(
    a_indices=constant_op.constant(0, shape=[17, 4], dtype=dtypes.int64),
    a_values=constant_op.constant(0, shape=[17], dtype=dtypes.float32),
    a_shape=constant_op.constant([3, 4], dtype=dtypes.int64),
    b=constant_op.constant(1, shape=[3, 4], dtype=dtypes.float32),
    expected_error="Dimensions 4 and 2 are not compatible")
self._testSparseDenseInvalidInputs(
    a_indices=constant_op.constant(7, shape=[17, 2], dtype=dtypes.int64),
    a_values=constant_op.constant(0, shape=[17], dtype=dtypes.float32),
    a_shape=constant_op.constant([3, 4], dtype=dtypes.int64),
    b=constant_op.constant(1, shape=[3, 4], dtype=dtypes.float32),
    expected_error="invalid index")
