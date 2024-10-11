# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
expected = np.eye(n, m)
if as_tensors:
    m = constant_op.constant(m)
    n = constant_op.constant(n)
s = sparse_ops.sparse_eye(n, m)
d = sparse_ops.sparse_to_dense(s.indices, s.dense_shape, s.values)
self.assertAllEqual(self.evaluate(d), expected)
