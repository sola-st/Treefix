# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
n = len(args)
output = []
for i, a in enumerate(args):
    a = asarray(a)
    a_rank = array_ops.rank(a)
    a_rank_temp = np_utils.get_static_value(a_rank)
    if a_rank_temp is not None:
        a_rank = a_rank_temp
        if a_rank != 1:
            raise ValueError('Arguments must be 1-d, got arg {} of rank {}'.format(
                i, a_rank))
    else:
        control_flow_ops.Assert(math_ops.equal(a_rank, 1), [a_rank])

    new_shape = [1] * n
    new_shape[i] = -1
    dtype = a.dtype
    if dtype == dtypes.bool:
        output.append(array_ops.reshape(nonzero(a)[0], new_shape))
    elif dtype.is_integer:
        output.append(array_ops.reshape(a, new_shape))
    else:
        raise ValueError(
            'Only integer and bool dtypes are supported, got {}'.format(dtype))

exit(output)
