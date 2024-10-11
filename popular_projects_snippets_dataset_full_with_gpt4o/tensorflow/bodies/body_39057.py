# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
for dtype in [dtypes.complex64, dtypes.complex128]:
    tf_val = math_ops.cast(
        constant_op.constant([1.0 + 1.0j, 2.0 - 2.0j]), dtypes.complex128)
    tf_ans = sparse_ops.sparse_tensor_to_dense(sparse_ops.from_dense(tf_val))
    self.assertAllClose(tf_val, tf_ans)
