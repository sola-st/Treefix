# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(x)
    y = nn_ops.elu(x)
    dy = tape.gradient(y, x)
exit(tape.gradient(dy, x))
