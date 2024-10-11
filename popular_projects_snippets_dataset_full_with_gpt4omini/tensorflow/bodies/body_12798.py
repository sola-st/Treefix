# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with self.cached_session():
    data = indexed_slices.IndexedSlices(
        constant_op.constant([1, 2, 3]),
        constant_op.constant([0, 1, 2]),
        dense_shape=constant_op.constant([3]))
    zero = constant_op.constant(0)
    one = constant_op.constant(1)
    less_op = math_ops.less(zero, one)
    _, switch_true = control_flow_ops.switch(data, less_op)
    self.assertAllEqual([1, 2, 3], switch_true.values)
    self.assertAllEqual([0, 1, 2], switch_true.indices)
