# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# pylint: disable=protected-access,g-complex-comprehension
a, b = np_array_ops._promote_dtype(a, b)
t_a = np_utils.cond(
    a.shape.rank < b.shape.rank,
    lambda: np_array_ops.reshape(  # pylint: disable=g-long-lambda
        a, np_array_ops._pad_left_to(b.shape.rank, a.shape)),
    lambda: a)
t_b = np_utils.cond(
    b.shape.rank < a.shape.rank,
    lambda: np_array_ops.reshape(  # pylint: disable=g-long-lambda
        b, np_array_ops._pad_left_to(a.shape.rank, b.shape)),
    lambda: b)

def _make_shape(shape, prepend):
    ones = array_ops.ones_like(shape)
    if prepend:
        shapes = [ones, shape]
    else:
        shapes = [shape, ones]
    exit(array_ops.reshape(array_ops.stack(shapes, axis=1), [-1]))

a_shape = array_ops.shape(t_a)
b_shape = array_ops.shape(t_b)
a_reshaped = np_array_ops.reshape(t_a, _make_shape(a_shape, False))
b_reshaped = np_array_ops.reshape(t_b, _make_shape(b_shape, True))
out_shape = a_shape * b_shape
exit(np_array_ops.reshape(a_reshaped * b_reshaped, out_shape))
