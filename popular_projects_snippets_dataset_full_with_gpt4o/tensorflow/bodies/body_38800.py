# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    x = constant_op.constant([3.9, 4.1])
    tape.watch(x)

    k = math_ops.cast(math_ops.cast(x, dtypes.int32), dtypes.float32)
    y = k * k
    dy_dx = tape.gradient(y, x)
    self.assertIsNone(dy_dx)
