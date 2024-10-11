# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session(), self.test_scope():
    tf_ans = _SparseToDense([1, 3], [5], 1, -1)
np_ans = np.array([-1, 1, -1, 1, -1]).astype(np.int32)
self.assertAllClose(np_ans, tf_ans)
