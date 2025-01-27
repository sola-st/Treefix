# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
config = config_pb2.ConfigProto(device_count={"CPU": 2},
                                allow_soft_placement=True)
with self.cached_session(config=config) as sess:
    pred = array_ops.placeholder(dtypes.bool, [])
    x_init = constant_op.constant(1.0)

    with ops.device("/cpu:0"):
        z = control_flow_ops.while_loop(
            lambda i, _: i < 3,
            lambda i, x: (i + 1, control_flow_ops.cond(
                pred, lambda: x * 2.0, lambda: 10.0)),
            [0, x_init])

    with ops.device("/cpu:1"):
        grad = gradients_impl.gradients(z, x_init)[0]

    with ops.device("/cpu:0"):
        grad_grad = gradients_impl.gradients(grad, x_init)[0]

    self.assertEqual(sess.run(grad, {pred: True}), 8.0)
    self.assertEqual(sess.run(grad, {pred: False}), 0.0)

    if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
        exit()

    self.assertEqual(sess.run(grad_grad, {pred: True}), 0.0)
    self.assertEqual(sess.run(grad_grad, {pred: False}), 0.0)
