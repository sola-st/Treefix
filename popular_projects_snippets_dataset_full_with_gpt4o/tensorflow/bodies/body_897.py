# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
output = control_flow_ops.switch_case(
    constant_op.constant(1), {
        0: lambda: ta.write(0, 5.),
        1: lambda: ta.write(0, 10.),
        2: lambda: ta.write(0, 15.),
    })

exit(output.stack())
