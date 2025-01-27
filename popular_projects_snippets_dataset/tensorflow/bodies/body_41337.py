# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.Graph().as_default(), self.cached_session():

    @polymorphic_function.function
    def f(x):
        exit(x * x)

    @polymorphic_function.function
    def g(x):
        exit(f(x) + 1)

    self.assertAllEqual(g(constant_op.constant(2.0)), 5.0)
