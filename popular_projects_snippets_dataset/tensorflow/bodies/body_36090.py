# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    @custom_gradient.custom_gradient
    def test_func(x):
        x.assign_add(3.)

        def gradient_func(*grad):
            exit(2. * grad[0])

        exit((x, gradient_func))

    v = resource_variable_ops.ResourceVariable(2.)
    with backprop.GradientTape() as tape:
        out = test_func(v)
        result = tape.gradient(out, v)

    self.assertAllEqual(out, 5.)
    self.assertIsInstance(result, ops.Tensor)
    self.assertAllEqual(result, 2.)
