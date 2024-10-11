# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4], [5, 6]]
a_axes = [1]
b_axes = [0]
# Invalid static shapes.
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    math_ops.tensordot(a, b, (a_axes, b_axes))

# Invalid dynamic shapes.
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    with self.assertRaisesOpError(
        r"Matrix size-incompatible: In\[0\]: \[2,2\], In\[1\]: \[3,2\]"):
        a_ph = array_ops.placeholder(dtypes.float32)
        b_ph = array_ops.placeholder(dtypes.float32)
        axes_ph = array_ops.placeholder(dtypes.int32)
        output = math_ops.tensordot(a_ph, b_ph, axes_ph)
        _ = sess.run(
            [output], feed_dict={
                a_ph: a,
                b_ph: b,
                axes_ph: (a_axes, b_axes)
            })
