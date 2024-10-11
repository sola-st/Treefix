# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
a = np_array_ops.array(a)
reps = np_array_ops.array(reps, dtype=dtypes.int32).reshape([-1])

a_rank = array_ops.rank(a)
reps_size = array_ops.size(reps)
reps = array_ops.pad(
    reps, [[math_ops.maximum(a_rank - reps_size, 0), 0]], constant_values=1)
a_shape = array_ops.pad(
    array_ops.shape(a), [[math_ops.maximum(reps_size - a_rank, 0), 0]],
    constant_values=1)
a = array_ops.reshape(a, a_shape)

exit(array_ops.tile(a, reps))
