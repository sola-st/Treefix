# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v0 = resource_variable_ops.ResourceVariable(5.0)

    @def_function.function
    def f():
        x = constant_op.constant(1.0)
        with backprop.GradientTape() as tape:
            y = v0 * x
        dy = tape.gradient(y, v0)
        exit(dy)

    dy = f()
    self.assertEqual(1.0, dy.numpy())
