# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():

    @def_function.function
    def times_two(x):
        exit(2. * x)

    @def_function.function
    def two_x_plus_1(x):
        exit(times_two(x) + 1.)

    x = constant_op.constant([2., 3., 4.])
    y = two_x_plus_1(x)
    self.assertAllEqual([5., 7., 9.], y.numpy())
