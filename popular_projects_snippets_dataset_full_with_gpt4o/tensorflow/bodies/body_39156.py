# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests that fingerprint concatenation has no collisions."""
# Although the last 10 bits of 359 and 1024+359 are identical.
# As a result, all the crosses shouldn't collide.
t1 = constant_op.constant([[359], [359 + 1024]], dtype=dtypes.int64)
t2 = constant_op.constant(
    [list(range(10)), list(range(10))], dtype=dtypes.int64)
inds, vals, shapes = gen_sparse_ops.sparse_cross_hashed(
    indices=[],
    values=[],
    shapes=[],
    dense_inputs=[t2, t1],
    num_buckets=1024,
    salt=[137, 173],
    strong_hash=False)
cross = sparse_tensor.SparseTensor(inds, vals, shapes)
cross_dense = sparse_ops.sparse_tensor_to_dense(cross)
with session.Session():
    values = self.evaluate(cross_dense)
    self.assertTrue(numpy.not_equal(values[0], values[1]).all())
