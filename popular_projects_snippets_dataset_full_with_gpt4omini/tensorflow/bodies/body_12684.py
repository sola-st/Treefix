# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
assert x.dtype == dtypes.float32
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = nn_ops.softmax(x)
exit(tape.gradient(y, x))
