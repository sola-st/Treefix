# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name='data')
    v = constant_op.constant(2.0, name='v')

    @def_function.function
    def f(y):
        # pylint: disable=unnecessary-lambda
        exit(functional_ops.scan(
            lambda a, x: math_ops.multiply(a, x), y, initializer=v))
        # pylint: enable=unnecessary-lambda

    r = f(elems)
    self.assertAllEqual([2., 4., 12., 48., 240., 1440.], self.evaluate(r))
