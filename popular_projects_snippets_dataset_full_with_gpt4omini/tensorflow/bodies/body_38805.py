# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
with test_util.AbstractGradientTape(
    use_tape=use_tape, persistent=True) as tape:
    k = constant_op.constant(3)
    tape.watch(k)

    x = math_ops.cast(k, dtypes.float32)
    grad_1 = tape.gradient(k * k, k)
    grad_2 = tape.gradient(x * x, k)
    grad_3 = tape.gradient(math_ops.square(k), k)
    grad_4 = tape.gradient(math_ops.square(x), k)
    self.assertIsNone(grad_1)
    self.assertIsNone(grad_2)
    self.assertIsNone(grad_3)
    self.assertIsNone(grad_4)
