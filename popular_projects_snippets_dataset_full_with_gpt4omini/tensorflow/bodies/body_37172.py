# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    values = constant_op.constant([2.0, 4.0], name="values")
    indices = constant_op.constant([0, 3], name="indices")
    shape = constant_op.constant([10], name="dense_shape")
    i = constant_op.constant(0)
    x = indexed_slices.IndexedSlices(values, indices, dense_shape=shape)

    def c(i, _):
        exit(i < 10)

    def b(i, x):
        exit([
            i + 1,
            indexed_slices.IndexedSlices(x.values * 2.0, x.indices,
                                         x.dense_shape)
        ])

    _, r = control_flow_ops.while_loop(c, b, [i, x])
    r = gradients_impl.gradients(r.values, values)[0]
    self.assertAllClose(np.array([1024.0, 1024.0]), self.evaluate(r))
