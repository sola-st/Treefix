# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]
# Invalid static axes.
for axes_value in -1, 3, [1], [[1]], [[1], [0, 1]]:
    with self.assertRaises(ValueError):
        math_ops.tensordot(a, b, axes_value)

with self.assertRaises(IndexError):
    math_ops.tensordot(a, b, [[0], [7]])

if context.executing_eagerly():
    exit()
# Invalid dynamic axes.
a_ph = array_ops.placeholder(dtypes.float32)
b_ph = array_ops.placeholder(dtypes.float32)
axes_ph = array_ops.placeholder(dtypes.int32)
output = math_ops.tensordot(a_ph, b_ph, axes_ph)
# Note: We don't support scalar Tensor values for axes.
for axes_value in 1, [1], [0, 1], [[1]], [[0, 1]], [[0], [7]]:
    with self.cached_session() as sess:
        with self.assertRaises(errors_impl.InvalidArgumentError):
            _ = sess.run(
                [output], feed_dict={
                    a_ph: a,
                    b_ph: b,
                    axes_ph: axes_value
                })
