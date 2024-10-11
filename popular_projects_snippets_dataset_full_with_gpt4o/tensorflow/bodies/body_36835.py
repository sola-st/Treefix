# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    values = constant_op.constant([10])
    indices = constant_op.constant([0])
    x = indexed_slices.IndexedSlices(values, indices)
    pred = math_ops.less(1, 2)
    fn1 = lambda: indexed_slices.IndexedSlices(
        math_ops.add(x.values, 1), indices)
    fn2 = lambda: indexed_slices.IndexedSlices(
        math_ops.subtract(x.values, 1), indices)
    r = control_flow_ops.cond(pred, fn1, fn2)

    val = r.values
    ind = r.indices
self.assertAllEqual([11], val)
self.assertAllEqual([0], ind)
