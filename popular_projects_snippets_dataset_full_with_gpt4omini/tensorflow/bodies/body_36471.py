# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape() as tape:
    tape.watch(a)
    _, b = while_loop_v2(
        lambda i, _: i < 2,
        lambda i, y: (i + 1, math_ops.cos(v + y)),
        [0, a])
exit(tape.gradient(b, a))
