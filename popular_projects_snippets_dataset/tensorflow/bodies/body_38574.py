# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/division_future_test.py
"""Test all the different ways to divide."""
values = [1, 2, 7, 11]
functions = (lambda x: x), constant_op.constant
# TODO(irving): Test int8, int16 once we support casts for those.
dtypes = np.int32, np.int64, np.float32, np.float64

tensors = []
checks = []

def check(x, y):
    x = ops.convert_to_tensor(x)
    y = ops.convert_to_tensor(y)
    tensors.append((x, y))
    def f(x, y):
        self.assertEqual(x.dtype, y.dtype)
        self.assertAllClose(x, y)
    checks.append(f)

with self.cached_session() as sess:
    for dtype in dtypes:
        for x in map(dtype, values):
            for y in map(dtype, values):
                for fx in functions:
                    for fy in functions:
                        tf_x = fx(x)
                        tf_y = fy(y)
                        div = x / y
                        tf_div = tf_x / tf_y
                        check(div, tf_div)
                        floordiv = x // y
                        tf_floordiv = tf_x // tf_y
                        check(floordiv, tf_floordiv)
      # Do only one sess.run for speed
    for f, (x, y) in zip(checks, self.evaluate(tensors)):
        f(x, y)
