# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():

    x = constant_op.constant(1.0)
    y = constant_op.constant(10.0)
    with backprop.GradientTape(persistent=True) as tape:
        tape.watch(x)
        tape.watch(y)
        a = x + y + x * y
    da_dx = tape.gradient(a, x)
    da_dy = tape.gradient(a, y)

self.assertEqual(11.0, da_dx.numpy())
self.assertEqual(2.0, da_dy.numpy())
