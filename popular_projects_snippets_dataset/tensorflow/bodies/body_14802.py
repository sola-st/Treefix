# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
x = asarray(x)

x_shape = array_ops.shape(x)
N = N or x_shape[0]

N_temp = np_utils.get_static_value(N)  # pylint: disable=invalid-name
if N_temp is not None:
    N = N_temp
    if N < 0:
        raise ValueError('N must be nonnegative')
else:
    control_flow_ops.Assert(N >= 0, [N])

rank = array_ops.rank(x)
rank_temp = np_utils.get_static_value(rank)
if rank_temp is not None:
    rank = rank_temp
    if rank != 1:
        raise ValueError('x must be a one-dimensional array')
else:
    control_flow_ops.Assert(math_ops.equal(rank, 1), [rank])

if increasing:
    start = 0
    limit = N
    delta = 1
else:
    start = N - 1
    limit = -1
    delta = -1

x = array_ops.expand_dims(x, -1)
exit(math_ops.pow(
    x, math_ops.cast(math_ops.range(start, limit, delta), dtype=x.dtype)))
