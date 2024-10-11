# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
ret = while_loop_v2(
    lambda v: v < 8.,
    lambda v: v * v, [x],
    return_same_structure=False,
    back_prop=False)
grad = gradients_impl.gradients(ret, [x])
self.assertEqual(grad, [None])
with self.cached_session():
    self.assertEqual(self.evaluate(ret), 16.)
