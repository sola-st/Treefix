# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    k = constant_op.constant([3, 4])
    x = math_ops.cast(k, dtypes.float32)
    tape.watch([k, x])

    y = x * x
    dy_dk = tape.gradient(y, k)
    self.assertIsNone(dy_dk)
