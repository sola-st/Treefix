# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    # Create constant of shape [100, 2, 1]. This tensor would be
    # excessively padded on TPU.
    tensor = constant_op.constant(100 * [[[10.0], [2.0]]])
    # Use reduce_sum since it requires correctly working with
    # a particular dimension.
    reduced = math_ops.reduce_sum(tensor, axis=1)
    self.assertAllEqual(100 * [[12.0]], reduced)
