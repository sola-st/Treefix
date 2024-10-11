# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    x = constant_op.constant([1.0, -0.0], dtype=dtype)

    with backprop.GradientTape() as tape:
        tape.watch(x)
        y = math_ops.reduce_euclidean_norm(x)

    dx = tape.gradient(y, x)
    dx_answer = constant_op.constant([1.0, -0.0], dtype=dtype)
    self.assertAllClose(dx, dx_answer)
    self.assertAllClose(1.0 / dx, 1.0 / dx_answer)
