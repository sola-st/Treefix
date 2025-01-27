# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
with context.eager_mode():
    x = math_ops.complex(1., 1.)
    with backprop.GradientTape() as t:
        t.watch(x)
        y = math_ops.sign(x)
    self.assertAllClose(
        t.gradient(y, x), math_ops.complex(0.353553, -0.353553))
