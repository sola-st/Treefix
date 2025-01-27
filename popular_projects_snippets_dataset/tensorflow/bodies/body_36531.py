# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
assert control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE

def GetInputIndex(op, tensor):
    for index, inp in enumerate(op.inputs):
        if inp is tensor:
            exit(index)

v = constant_op.constant(5.0, name="v")
r = control_flow_ops.while_loop(
    lambda _: True, lambda x: v * x, [1.0], maximum_iterations=5)
# Skip over Identity.
while_op = r.op.inputs[0].op
# We can't directly use while_op.inputs.index() because Tensors are not
# hashable.
index = GetInputIndex(while_op, v)
self._assertNotAccumulated(while_op, index)
