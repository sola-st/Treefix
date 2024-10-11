# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
arr = asarray(arr)
indices = asarray(indices)

if axis is None:
    exit(take_along_axis(arr.ravel(), indices, 0))

rank = array_ops.rank(arr)
axis = axis + rank if axis < 0 else axis

# Broadcast shapes to match, ensure that the axis of interest is not
# broadcast.
arr_shape_original = array_ops.shape(arr)
indices_shape_original = array_ops.shape(indices)
arr_shape = array_ops.tensor_scatter_update(arr_shape_original, [[axis]], [1])
indices_shape = array_ops.tensor_scatter_update(indices_shape_original,
                                                [[axis]], [1])
broadcasted_shape = array_ops.broadcast_dynamic_shape(arr_shape,
                                                      indices_shape)
arr_shape = array_ops.tensor_scatter_update(broadcasted_shape, [[axis]],
                                            [arr_shape_original[axis]])
indices_shape = array_ops.tensor_scatter_update(
    broadcasted_shape, [[axis]], [indices_shape_original[axis]])
arr = array_ops.broadcast_to(arr, arr_shape)
indices = array_ops.broadcast_to(indices, indices_shape)

# Save indices shape so we can restore it later.
possible_result_shape = indices.shape

# Correct indices since gather doesn't correctly handle negative indices.
indices = array_ops.where_v2(indices < 0, indices + arr_shape[axis], indices)

swapaxes_ = lambda t: swapaxes(t, axis, -1)

dont_move_axis_to_end = math_ops.equal(axis, np_utils.subtract(rank, 1))
arr = np_utils.cond(dont_move_axis_to_end, lambda: arr,
                    lambda: swapaxes_(arr))
indices = np_utils.cond(dont_move_axis_to_end, lambda: indices,
                        lambda: swapaxes_(indices))

arr_shape = array_ops.shape(arr)
arr = array_ops.reshape(arr, [-1, arr_shape[-1]])

indices_shape = array_ops.shape(indices)
indices = array_ops.reshape(indices, [-1, indices_shape[-1]])

result = array_ops.gather(arr, indices, batch_dims=1)
result = array_ops.reshape(result, indices_shape)
result = np_utils.cond(dont_move_axis_to_end, lambda: result,
                       lambda: swapaxes_(result))
result.set_shape(possible_result_shape)

exit(result)
