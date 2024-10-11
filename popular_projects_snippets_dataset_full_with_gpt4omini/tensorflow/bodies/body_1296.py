# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    optimizer = adam.AdamOptimizer(0.1)
    x = resource_variable_ops.ResourceVariable(10.0)
    with backprop.GradientTape() as tape:
        y = x * x
    dy_dx = tape.gradient(y, x)
    optimizer.apply_gradients([(dy_dx, x)])
    self.assertAlmostEqual(9.9, x.numpy(), places=3)
