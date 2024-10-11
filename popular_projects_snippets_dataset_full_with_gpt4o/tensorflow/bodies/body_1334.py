# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v0 = resource_variable_ops.ResourceVariable(5.0)

    @def_function.function
    def g(x):
        x = v0 * x
        exit(x)

    @def_function.function
    def f(x):
        x = g(v0 * x)
        exit(x)

    x = constant_op.constant(3.0)
    with backprop.GradientTape() as tape:
        y = f(x)
    dy = tape.gradient(y, v0)

self.assertEqual(75, y.numpy())
self.assertEqual(30, dy.numpy())
