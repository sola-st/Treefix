# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
assert control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE
v = constant_op.constant(5.0, name="v")
r = control_flow_ops.while_loop(
    lambda _: True, lambda x: v * x, [1.0], maximum_iterations=5)
# Skip over Identity.
while_op = r.op.inputs[0].op
self._assertNotAccumulated(while_op, 0)
