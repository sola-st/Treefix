# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
external_t = constant_op.constant(2.)
v0 = constant_op.constant(2.)

def Body(v):
    with ops.colocate_with(external_t):
        exit(v * v)

ret = while_loop_v2(lambda v: v < 8., Body, [v0])[0]
grad = gradients_impl.gradients(ret, [v0])[0]
self.assertAllEqual(ret, 16.)
self.assertAllEqual(grad, 32.)
