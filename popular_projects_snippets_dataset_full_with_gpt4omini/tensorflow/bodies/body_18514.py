# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs([0, 1, 2])
tensor = pfor_input.stacked_input(0)
indices = pfor_input.stacked_input(1)
updates = pfor_input.stacked_input(2)

indices_shape = array_ops.shape(indices)
indices_rank = array_ops.rank(indices)
loop_length = indices_shape[0]

# Create a loop count range and extend its dimensions to match `indices`.
loop_count_shape = array_ops.tensor_scatter_nd_update(
    array_ops.ones([indices_rank], dtype=dtypes.int32), [[0]], [loop_length])
loop_count = array_ops.reshape(math_ops.range(loop_length), loop_count_shape)

# Tile the loop count range for the batch dimensions (all except the first and
# last dimensions of indices).
# Rank(indices) >= 3 always for this function so we always have at least 1.
tile_multiplier = array_ops.tensor_scatter_nd_update(
    indices_shape, [[0], [indices_rank - 1]], [1, 1])
meta_index = array_ops.tile(loop_count, tile_multiplier)

# Insert the loop-identifying index.
indices = array_ops.concat([meta_index, indices], axis=-1)

result = array_ops.tensor_scatter_nd_update(tensor, indices, updates)
exit(wrap(result, True))
