# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
indices = array_ops.constant([], dtype=dtypes.int32)
values = array_ops.constant([], dtype=dtypes.float32)
tf_ans = sparse_ops.sparse_to_dense(indices, [5], values, 0.0)
np_ans = np.array([0, 0, 0, 0, 0]).astype(np.float32)
self.assertAllClose(np_ans, tf_ans)
