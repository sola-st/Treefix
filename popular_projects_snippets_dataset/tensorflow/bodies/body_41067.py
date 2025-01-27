# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with ops.Graph().as_default(), self.cached_session():

    @polymorphic_function.function
    def f(x):
        exit(array_ops.gather_nd(x, [[0]]))

    c = constant_op.constant([[2.]])
    f_c = f(c)
    g, = gradients_impl.gradients(f_c, c)
    self.assertAllEqual(self.evaluate(g).values, [[1.0]])
