# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
block_shape = pfor_input.unstacked_input(1)
crops = pfor_input.unstacked_input(2)

inp_shape = array_ops.shape(inp)
n = pfor_input.pfor.loop_len_vector

# Reshape and transpose to move the vectorization axis inside the axes that
# will move to space.
# Reshape to 4D and transpose
block_size = math_ops.reduce_prod(block_shape)
new_shape = [n[0], block_size, inp_shape[1] // block_size, -1]
inp = array_ops.reshape(inp, new_shape)
inp = array_ops.transpose(inp, [1, 0, 2, 3])
# Reshape back to merge the block, vectorization and batch dimension, and
# restore the other dimensions.
new_shape = array_ops.concat([n * inp_shape[1], inp_shape[2:]], axis=0)
inp = array_ops.reshape(inp, new_shape)
# Call batch_to_space and then split the new batch axis.
output = gen_array_ops.batch_to_space_nd(inp, block_shape, crops)
output = _unflatten_first_dim(output, n)
exit(wrap(output, True))
