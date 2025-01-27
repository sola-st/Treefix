# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    values = constant_op.constant([10])
    i_32 = ops.convert_to_tensor([0], name="one", dtype=dtypes.int32)
    i_64 = ops.convert_to_tensor([0], name="one", dtype=dtypes.int64)
    x = indexed_slices.IndexedSlices(values, i_32)
    pred = math_ops.less(1, 2)
    fn1 = lambda: indexed_slices.IndexedSlices(
        math_ops.add(x.values, 1), i_32)
    fn2 = lambda: indexed_slices.IndexedSlices(
        math_ops.subtract(x.values, 1), i_64)
    r = control_flow_ops.cond(pred, fn1, fn2)

    val = r.values
    ind = r.indices
self.assertAllEqual([11], val)
self.assertAllEqual([0], ind)
self.assertTrue(ind.dtype == np.int64)
