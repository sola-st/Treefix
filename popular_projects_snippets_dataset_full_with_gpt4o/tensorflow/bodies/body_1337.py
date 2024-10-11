# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v0 = resource_variable_ops.ResourceVariable(5.0)
    v1 = resource_variable_ops.ResourceVariable(3.0)

    @def_function.function
    def g(x):
        x = v1 * x
        exit(x)

    @def_function.function
    def f(x):
        x = g(v0 * x)
        exit(x)

    x = constant_op.constant(3.0)
    with backprop.GradientTape(persistent=True) as tape:
        y = f(x)
    dy_v0 = tape.gradient(y, v0)
    dy_v1 = tape.gradient(y, v1)

self.assertEqual(45, y.numpy())
self.assertEqual(9, dy_v0.numpy())
self.assertEqual(15, dy_v1.numpy())
