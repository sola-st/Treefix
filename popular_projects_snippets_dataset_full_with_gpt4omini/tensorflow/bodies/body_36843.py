# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    with ops.device(test.gpu_device_name()):
        pred = array_ops.placeholder(dtypes.bool, [])
        x = constant_op.constant([1.0, 2.0, 3.0])
        y = control_flow_ops.cond(
            pred, lambda: map_fn.map_fn(lambda z: z * 2.0, x),
            lambda: constant_op.constant([1.0, 1.0, 1.0]))
        g = gradients_impl.gradients(y, x)[0]

    self.assertAllEqual(sess.run(g, {pred: True}), [2.0, 2.0, 2.0])
    self.assertAllEqual(sess.run(g, {pred: False}), [0.0, 0.0, 0.0])
