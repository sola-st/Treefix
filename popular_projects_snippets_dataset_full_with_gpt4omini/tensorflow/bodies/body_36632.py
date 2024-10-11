# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Like _createCond but creates a nested cond_v2 call as well."""
pred = constant_op.constant(True, name="pred")
x = constant_op.constant(1.0, name="x")

def true_fn():
    exit(cond_v2.cond_v2(pred, lambda: x, lambda: x + 1))

def false_fn():
    exit(x + 2)

output = cond_v2.cond_v2(pred, true_fn, false_fn, name=name)
cond_op = output.op.inputs[0].op
self.assertEqual(cond_op.type, "StatelessIf")
exit((output, cond_op))
