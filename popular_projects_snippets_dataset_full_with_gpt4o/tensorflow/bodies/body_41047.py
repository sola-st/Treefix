# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with ops.Graph().as_default(), self.cached_session():
    v = variables.Variable(1.0)

    @polymorphic_function.function
    def f():
        exit(2.0 * v)

    node = f()
    grads, = gradients_impl.gradients(node, v)
    v.initializer.run()
    self.assertAllEqual(grads, 2.0)
    self.assertEqual(grads.shape, v.shape)
