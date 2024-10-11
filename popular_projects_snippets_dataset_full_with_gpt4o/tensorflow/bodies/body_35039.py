# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
# This should only be detected as an integer.
x = array_ops.placeholder(dtypes.float32)
y = array_ops.placeholder(dtypes.float32)
# First component isn't less than float32.eps = 1e-7
z = array_ops.placeholder(dtypes.float32)
# This shouldn"t be detected as an integer.
w = array_ops.placeholder(dtypes.float32)
feed_dict = {x: [1., 5, 10, 15, 20], y: [1.1, 5, 10, 15, 20],
             z: [1.0001, 5, 10, 15, 20], w: [1e-8, 5, 10, 15, 20]}
with self.cached_session():
    with ops.control_dependencies([du.assert_integer_form(x)]):
        array_ops.identity(x).eval(feed_dict=feed_dict)

    with self.assertRaisesOpError("has non-integer components"):
        with ops.control_dependencies(
            [du.assert_integer_form(y)]):
            array_ops.identity(y).eval(feed_dict=feed_dict)

    with self.assertRaisesOpError("has non-integer components"):
        with ops.control_dependencies(
            [du.assert_integer_form(z)]):
            array_ops.identity(z).eval(feed_dict=feed_dict)

    with self.assertRaisesOpError("has non-integer components"):
        with ops.control_dependencies(
            [du.assert_integer_form(w)]):
            array_ops.identity(w).eval(feed_dict=feed_dict)
