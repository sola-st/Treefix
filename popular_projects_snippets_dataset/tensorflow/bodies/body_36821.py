# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    values = constant_op.constant([1, 2, 3, 4, 5, 6])
    indices = constant_op.constant([0, 2, 4, 6, 8, 10])
    data = indexed_slices.IndexedSlices(values, indices)
    pred = ops.convert_to_tensor(True)
    switch_op = control_flow_ops.switch(data, pred)
    merge_op = control_flow_ops.merge(switch_op)[0]

    val = merge_op.values
    ind = merge_op.indices
self.assertAllEqual(np.arange(1, 7), val)
self.assertAllEqual(np.arange(0, 12, 2), ind)
