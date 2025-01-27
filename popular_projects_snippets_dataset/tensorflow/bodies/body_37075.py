# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
v0 = constant_op.constant(2.)
r = control_flow_ops.while_loop(
    lambda _: True, lambda v: v * v, [v0], maximum_iterations=3)

self.assertAllEqual(r, 256.)
grad = gradients_impl.gradients(r, v0)[0]
self.assertAllClose(grad, 1024.)
