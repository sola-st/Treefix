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
    y = f(x)

self.assertEqual(75.0, y.numpy())
