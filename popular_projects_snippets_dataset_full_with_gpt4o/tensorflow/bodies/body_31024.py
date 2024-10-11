# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
assert x.dtype == dtypes.float32
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = nn_ops.leaky_relu(x)
exit(tape.gradient(y, x))
