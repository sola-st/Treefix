# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
tf_ans = sparse_ops.sparse_to_dense([[1, 3, 0], [2, 0, 1]], [3, 4, 2], 1,
                                    -1)
np_ans = np.ones((3, 4, 2), dtype=np.int32) * -1
np_ans[1, 3, 0] = 1
np_ans[2, 0, 1] = 1
self.assertAllClose(np_ans, tf_ans)
