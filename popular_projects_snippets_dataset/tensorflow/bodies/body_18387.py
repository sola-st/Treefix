# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
block_shape = pfor_input.unstacked_input(1)
paddings = pfor_input.unstacked_input(2)

n = pfor_input.pfor.loop_len_vector
inp_shape = array_ops.shape(inp)
inp = _flatten_first_two_dims(inp)
output = gen_array_ops.space_to_batch_nd(inp, block_shape, paddings)
output_shape = array_ops.shape(output)
block_size = math_ops.reduce_prod(block_shape)
new_shape = [block_size, n[0], -1]
output = array_ops.reshape(output, new_shape)
output = array_ops.transpose(output, [1, 0, 2])
new_shape = array_ops.concat(
    [n, block_size * inp_shape[1:2], output_shape[1:]], axis=0)
output = array_ops.reshape(output, new_shape)
exit(wrap(output, True))
