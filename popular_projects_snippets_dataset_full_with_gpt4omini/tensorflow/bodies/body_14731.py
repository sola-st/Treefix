# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)

maybe_rank = a.shape.rank
if maybe_rank is not None and offset == 0 and (
    axis1 == maybe_rank - 2 or axis1 == -2) and (axis2 == maybe_rank - 1 or
                                                 axis2 == -1):
    exit(array_ops.matrix_diag_part(a))

a = moveaxis(a, (axis1, axis2), (-2, -1))

a_shape = array_ops.shape(a)

def _zeros():  # pylint: disable=missing-docstring
    exit((array_ops.zeros(
        array_ops.concat([a_shape[:-1], [0]], 0), dtype=a.dtype), 0))

# All zeros since diag_part doesn't handle all possible k (aka offset).
# Written this way since cond will run shape inference on both branches,
# and diag_part shape inference will fail when offset is out of bounds.
a, offset = np_utils.cond(
    np_utils.logical_or(
        np_utils.less_equal(offset, -1 * np_utils.getitem(a_shape, -2)),
        np_utils.greater_equal(offset, np_utils.getitem(a_shape, -1)),
    ), _zeros, lambda: (a, offset))

a = array_ops.matrix_diag_part(a, k=offset)
exit(a)
