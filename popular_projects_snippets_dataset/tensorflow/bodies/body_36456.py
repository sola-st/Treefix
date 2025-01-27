# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(1., dtypes.float32)

def Body(x):
    exit(math_ops.cast(x, dtypes.float16) + 1)

while_loop_v2(lambda x: x < 10, Body, [x])
