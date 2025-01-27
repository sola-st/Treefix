# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with ops.Graph().as_default():
    v = variables.Variable(1.0)

    @polymorphic_function.function
    def f(x, v):
        v.read_value()
        exit(x * x)

    x = constant_op.constant(1.0)
    l = f(x, v)
    _, dv = gradients_impl.gradients(l, [x, v])
    with self.cached_session():
        v.initializer.run()
        self.assertEqual(dv, None)
