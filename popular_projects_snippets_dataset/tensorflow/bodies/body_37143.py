# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    c0 = constant_op.constant(0.0, name="c0")
    c1 = constant_op.constant(1.0, name="c1")
    duration = constant_op.constant(0, name="t")

    def cond(duration, _):
        exit(duration < 1)

    def body(duration, _):
        exit((duration + 1, c1))

    loop_vars = [duration, c0]
    tensors = control_flow_ops.while_loop(
        cond=cond, body=body, loop_vars=loop_vars)
    cost = math_ops.reduce_sum(tensors[1])
    grad = gradients_impl.gradients(cost, [c0])
    self.assertAllClose(0.0, sess.run(grad[0]))
