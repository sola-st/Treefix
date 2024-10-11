# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = math_ops.square(x)
    z = math_ops.square(y)
exit(tape.gradient(z, x))
