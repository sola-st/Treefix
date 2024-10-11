# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(3.0, name="y")

def true_fn():
    exit(((x * y,), y))

def false_fn():
    exit(((x,), y * 3.0))

output = control_flow_ops.cond(
    constant_op.constant(False), true_fn, false_fn)
self.assertEqual(self.evaluate(output[0][0]), 1.)
self.assertEqual(self.evaluate(output[1]), 9.)
