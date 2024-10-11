# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
config = config_pb2.ConfigProto(device_count={"CPU": 2},
                                allow_soft_placement=True)
with self.cached_session(config=config) as sess:
    pred = array_ops.placeholder(dtypes.bool, [])
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.placeholder(dtypes.float32)

    with ops.device("/cpu:0"):
        z = control_flow_ops.cond(pred, lambda: x * y * 2.0, lambda: 2.0)

    with ops.device("/cpu:1"):
        grad = gradients_impl.gradients(z, x)[0]

    with ops.device("/cpu:0"):
        grad_grad = gradients_impl.gradients(grad, x)[0]

    self.assertEqual(sess.run(grad, {pred: True, x: 1.0, y: 2.0}), 4.0)
    self.assertEqual(sess.run(grad, {pred: False, x: 1.0, y: 2.0}), 0.0)

    # v1 control flow gets None second derivative for some reason.
    if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
        self.assertIsNone(grad_grad)
        exit()

    self.assertEqual(sess.run(grad_grad, {pred: True, x: 1.0, y: 2.0}), 0.0)
    self.assertEqual(sess.run(grad_grad, {pred: False, x: 1.0, y: 2.0}), 0.0)
