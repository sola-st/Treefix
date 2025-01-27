# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
grad = pfor_input.stacked_input(0)
indices = pfor_input.unstacked_input(1)
segment_ids = pfor_input.unstacked_input(2)
dim0 = pfor_input.unstacked_input(3)

n = pfor_input.pfor.loop_len_vector[0]
indices = _flatten_array_with_offset(indices, dim0, n)
num_segments = nn_ops.relu(math_ops.reduce_max(segment_ids) + 1)
segment_ids = _flatten_array_with_offset(segment_ids, num_segments, n)
grad = _flatten_first_two_dims(grad)
dim0 *= n
output = op_func(grad, indices, segment_ids, dim0)
output = _unflatten_first_dim(output, [n])
exit(wrap(output, True))
