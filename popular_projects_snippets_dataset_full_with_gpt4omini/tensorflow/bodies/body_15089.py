# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x = ragged_factory_ops.constant([[1.0, 2.0], [3.0]])

with backprop.GradientTape() as t2:
    t2.watch(x)
    with backprop.GradientTape() as t1:
        t1.watch(x)
        y = x * x * x
    dy_dx = t1.gradient(y, x)
d2y_dx2 = t2.gradient(dy_dx, x)

self.assertAllEqual(dy_dx, [[3.0, 12.0], [27.0]])
self.assertAllEqual(d2y_dx2, [[6.0, 12.0], [18.0]])
