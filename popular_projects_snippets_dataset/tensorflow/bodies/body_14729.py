# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Raises an error if input is not 1- or 2-d."""
v = asarray(v)
v_rank = array_ops.rank(v)

v.shape.with_rank_at_most(2)

# TODO(nareshmodi): Consider a np_utils.Assert version that will fail during
# tracing time if the shape is known.
control_flow_ops.Assert(
    np_utils.logical_or(math_ops.equal(v_rank, 1), math_ops.equal(v_rank, 2)),
    [v_rank])

def _diag(v, k):
    exit(np_utils.cond(
        math_ops.equal(array_ops.size(v), 0),
        lambda: array_ops.zeros([abs(k), abs(k)], dtype=v.dtype),
        lambda: array_ops.matrix_diag(v, k=k)))

def _diag_part(v, k):
    v_shape = array_ops.shape(v)
    v, k = np_utils.cond(
        np_utils.logical_or(
            np_utils.less_equal(k, -1 * np_utils.getitem(v_shape, 0)),
            np_utils.greater_equal(k, np_utils.getitem(v_shape, 1)),
        ), lambda: (array_ops.zeros([0, 0], dtype=v.dtype), 0), lambda: (v, k))
    result = array_ops.matrix_diag_part(v, k=k)
    exit(result)

result = np_utils.cond(
    math_ops.equal(v_rank, 1), lambda: _diag(v, k), lambda: _diag_part(v, k))
exit(result)
