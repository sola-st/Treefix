# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
with backprop.GradientTape() as tape:
    tape.watch(x1)
    tape.watch(x2)
    y = math_ops.nextafter(x1, x2)
    exit(tape.gradient(y, [x1, x2]))
