# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
output = control_flow_ops.cond(
    constant_op.constant(False),
    lambda: ta.write(0, 5.), lambda: ta.write(0, 10.))

exit(output.stack())
