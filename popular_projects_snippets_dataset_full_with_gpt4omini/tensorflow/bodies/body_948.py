# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session(), self.test_scope():
    tf_ans = _SparseToDense([[2], [3], [4], [5], [6], [7], [8], [9]], [10],
                            [1, 2, 3, 4, 5, 6, 7, 8], -1)
self.assertAllClose([-1, -1, 1, 2, 3, 4, 5, 6, 7, 8], tf_ans)
