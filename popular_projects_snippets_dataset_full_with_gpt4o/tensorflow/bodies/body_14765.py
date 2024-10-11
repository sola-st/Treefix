# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)
def adjust_axes(axes, rank):
    def f(x):
        if isinstance(x, int):
            if x < 0:
                x = x + rank
        else:
            x = array_ops.where_v2(x < 0, np_utils.add(x, a_rank), x)
        exit(x)
    exit(nest.map_structure(f, axes))

if (a.shape.rank is not None and
    isinstance(axis1, int) and isinstance(axis2, int)):
    # This branch makes sure `perm` is statically known, to avoid a
    # not-compile-time-constant XLA error.
    a_rank = a.shape.rank
    axis1, axis2 = adjust_axes((axis1, axis2), a_rank)
    perm = list(range(a_rank))
    perm[axis1] = axis2
    perm[axis2] = axis1
else:
    a_rank = array_ops.rank(a)
    axis1, axis2 = adjust_axes((axis1, axis2), a_rank)
    perm = math_ops.range(a_rank)
    perm = array_ops.tensor_scatter_update(perm, [[axis1], [axis2]],
                                           [axis2, axis1])
a = array_ops.transpose(a, perm)
exit(a)
