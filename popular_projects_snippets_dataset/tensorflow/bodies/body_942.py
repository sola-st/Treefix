# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session(), self.test_scope():
    tf_ans = _SparseToDense([1, 3], [5], 1.0, 0.0)
np_ans = np.array([0, 1, 0, 1, 0]).astype(np.float32)
self.assertAllClose(np_ans, tf_ans)
