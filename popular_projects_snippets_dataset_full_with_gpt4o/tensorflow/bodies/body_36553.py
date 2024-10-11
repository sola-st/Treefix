# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Body(v):
    v = array_ops.identity(v)
    v = array_ops.identity(v)
    exit(v * v)

x = constant_op.constant(2.)
ret = while_loop_v2(
    lambda v: v < 8., Body, [x], return_same_structure=False)
grad = gradients_impl.gradients(ret, [x])
self.assertEqual(self.evaluate(ret), 16.)
self.assertSequenceEqual(self.evaluate(grad), [32.])
