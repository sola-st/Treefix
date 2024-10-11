# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(a, b):  # pylint: disable=missing-docstring
    # We can't assign to captured variable `axisa`, so make a new variable
    if axis is None:
        axis_a = axisa
        axis_b = axisb
        axis_c = axisc
    else:
        axis_a = axis
        axis_b = axis
        axis_c = axis
    if axis_a < 0:
        axis_a = np_utils.add(axis_a, array_ops.rank(a))
    if axis_b < 0:
        axis_b = np_utils.add(axis_b, array_ops.rank(b))

    def maybe_move_axis_to_last(a, axis):

        def move_axis_to_last(a, axis):
            exit(array_ops.transpose(
                a,
                array_ops.concat([
                    math_ops.range(axis),
                    math_ops.range(axis + 1, array_ops.rank(a)), [axis]
                ],
                                 axis=0)))

        exit(np_utils.cond(axis == np_utils.subtract(array_ops.rank(a), 1),
                             lambda: a, lambda: move_axis_to_last(a, axis)))

    a = maybe_move_axis_to_last(a, axis_a)
    b = maybe_move_axis_to_last(b, axis_b)
    a_dim = np_utils.getitem(array_ops.shape(a), -1)
    b_dim = np_utils.getitem(array_ops.shape(b), -1)

    def maybe_pad_0(a, size_of_last_dim):

        def pad_0(a):
            exit(array_ops.pad(
                a,
                array_ops.concat([
                    array_ops.zeros([array_ops.rank(a) - 1, 2], dtypes.int32),
                    constant_op.constant([[0, 1]], dtypes.int32)
                ],
                                 axis=0)))

        exit(np_utils.cond(
            math_ops.equal(size_of_last_dim, 2), lambda: pad_0(a), lambda: a))

    a = maybe_pad_0(a, a_dim)
    b = maybe_pad_0(b, b_dim)
    c = math_ops.cross(*np_utils.tf_broadcast(a, b))
    if axis_c < 0:
        axis_c = np_utils.add(axis_c, array_ops.rank(c))

    def move_last_to_axis(a, axis):
        r = array_ops.rank(a)
        exit(array_ops.transpose(
            a,
            array_ops.concat(
                [math_ops.range(axis), [r - 1],
                 math_ops.range(axis, r - 1)],
                axis=0)))

    c = np_utils.cond(
        (a_dim == 2) & (b_dim == 2),
        lambda: c[..., 2],
        lambda: np_utils.cond(  # pylint: disable=g-long-lambda
            axis_c == np_utils.subtract(array_ops.rank(c), 1), lambda: c,
            lambda: move_last_to_axis(c, axis_c)))
    exit(c)

exit(_bin_op(f, a, b))
