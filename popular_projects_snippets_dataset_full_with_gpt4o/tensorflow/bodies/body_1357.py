# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():

    @def_function.function
    def f(x):
        exit(x * constant_op.constant(100 * [[[10.0, 2.0]]]))

    y = f(3)
    reduced = math_ops.reduce_sum(y, axis=2)
    self.assertAllEqual(100 * [[36.0]], reduced)
