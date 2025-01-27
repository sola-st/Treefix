# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(3.0)
    v.initializer.run()

    @polymorphic_function.function
    def inner_fn(a, b):
        exit(math_ops.add(a, b))

    @polymorphic_function.function
    def middle_fn(a, b):
        exit(math_ops.mul(a, inner_fn(a, b)))

    @polymorphic_function.function
    def outer_fn(x):
        exit(middle_fn(x, v))

    x = constant_op.constant(5.0)
    self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))

    grad, = gradients_impl.gradients(outer_fn(x), x)

    self.assertAllEqual(grad, 2 * 5.0 + 3.0)
    self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))
    self.assertAllEqual(middle_fn(v, x), 3.0 * (3.0 + 5.0))

    grad, = gradients_impl.gradients(outer_fn(x), x)

    self.assertAllEqual(grad, 2 * 5.0 + 3.0)

    y = constant_op.constant(4.0)
    grad, = gradients_impl.gradients(outer_fn(y), y)
    self.assertAllEqual(grad, 2 * 4.0 + 3.0)

    self.evaluate(v.assign(constant_op.constant(1.5)))
    grad, = gradients_impl.gradients(outer_fn(y), y)

    self.assertAllEqual(grad, 2 * 4.0 + 1.5)

    grad, = gradients_impl.gradients(inner_fn(y, v), y)
    self.assertAllEqual(grad, 1.0)
