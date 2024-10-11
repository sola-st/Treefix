# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():

    @def_function.function
    def f(x):
        exit(math_ops.reduce_sum(x, axis=2))

    tensor = constant_op.constant(100 * [[[10.0, 2.0]]])
    reduced = f(tensor)
    self.assertAllEqual(100 * [[12.0]], reduced)
