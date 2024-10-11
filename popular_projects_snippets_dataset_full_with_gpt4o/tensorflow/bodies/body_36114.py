# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
"""Expects an error if an initializer is in a control-flow scope."""

def cond(i, _):
    exit(i < 10)

def body(i, _):
    zero = array_ops.zeros([], dtype=dtypes.int32)
    v = resource_variable_ops.ResourceVariable(initial_value=zero)
    exit((i + 1, v.read_value()))

with self.assertRaisesRegex(ValueError, "initial_value"):
    control_flow_ops.while_loop(cond, body, [0, 0])
