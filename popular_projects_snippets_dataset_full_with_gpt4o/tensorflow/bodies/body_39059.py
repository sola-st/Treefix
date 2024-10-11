# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
tf_ans = sparse_ops.sparse_to_dense([1, 3], [5], "a", "b")
np_ans = np.array(["b", "a", "b", "a", "b"]).astype(np.string_)
self.assertAllEqual(np_ans, tf_ans)
