# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests that fingerprint concatenation has no collisions."""
# Although the last 10 bits of 359 and 1024+359 are identical.
# As a result, all the crosses shouldn't collide.
t1 = constant_op.constant([[359], [359 + 1024]])
t2 = constant_op.constant([list(range(10)), list(range(10))])
cross = sparse_ops.sparse_cross_hashed(
    [t2, t1], num_buckets=1024, hash_key=sparse_ops._DEFAULT_HASH_KEY + 1)
cross_dense = sparse_ops.sparse_tensor_to_dense(cross)
with session.Session():
    values = self.evaluate(cross_dense)
    self.assertTrue(numpy.not_equal(values[0], values[1]).all())
