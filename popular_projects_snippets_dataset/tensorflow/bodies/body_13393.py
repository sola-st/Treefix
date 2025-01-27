# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
# Test case for GitHub issue 40633.
tensor = constant_op.constant(list('ababa'))
sparse = sparse_ops.from_dense(tensor)
result = self.evaluate(sparse)
self.assertAllEqual([[0], [1], [2], [3], [4]], result.indices)
self.assertAllEqual([b'a', b'b', b'a', b'b', b'a'], result.values)
self.assertAllEqual([5], result.dense_shape)
