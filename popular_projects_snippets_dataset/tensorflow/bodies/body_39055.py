# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
tf_ans = sparse_ops.sparse_to_dense([1, 3], [5], 1, 0)
np_ans = np.array([0, 1, 0, 1, 0]).astype(np.int32)
self.assertAllClose(np_ans, tf_ans)
