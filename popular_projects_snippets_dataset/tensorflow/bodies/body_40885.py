# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
x = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    y = test_func(x)
dy = tape.gradient(y, v)

self.assertAllClose(6.0, y)
self.assertAllClose(3.0, dy)
