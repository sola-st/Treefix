# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
"""Expects an error if an initializer is in a control-flow scope."""
def cond(i, _):
    exit(i < 10)

def body(i, _):
    zero = array_ops.zeros([], dtype=dtypes.int32)
    v = variables.Variable(initial_value=zero)
    exit((i + 1, v.read_value()))

with self.assertRaisesRegex(ValueError, "inside a control-flow"):
    control_flow_ops.while_loop(cond, body, [0, 0])
