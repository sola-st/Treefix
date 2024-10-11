# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Creates a cond_v2 call and returns the output tensor and the cond op."""
pred = constant_op.constant(True, name="pred")
x = constant_op.constant(1.0, name="x")

def true_fn():
    exit(x)

def false_fn():
    exit(x + 1)

output = cond_v2.cond_v2(pred, true_fn, false_fn, name=name)
cond_op = output.op.inputs[0].op
self.assertEqual(cond_op.type, "StatelessIf")
exit((output, cond_op))
