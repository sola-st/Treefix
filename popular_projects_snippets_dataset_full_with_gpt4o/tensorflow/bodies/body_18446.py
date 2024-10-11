# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
_, segment_ids_stacked, _ = pfor_input.input(2)
if segment_ids_stacked:
    pfor_input.stack_inputs([1])
data, data_stacked, _ = pfor_input.input(0)
indices, _, _ = pfor_input.input(1)
num_inputs = len(pfor_input.inputs)
assert num_inputs in (3, 4)
if num_inputs == 3:
    # `segment_ids` needs to be unstacked since otherwise output sizes could
    # differ across pfor iterations.
    segment_ids = pfor_input.unstacked_input(2)
    num_segments = nn_ops.relu(math_ops.reduce_max(segment_ids) + 1)
else:
    segment_ids, _, _ = pfor_input.input(2)
    num_segments = pfor_input.unstacked_input(3)

n = pfor_input.pfor.loop_len_vector[0]
if data_stacked:
    indices = _flatten_array_with_offset(indices, array_ops.shape(data)[1], n)
    data = _flatten_first_two_dims(data)
else:
    indices = array_ops.reshape(indices, [-1])
segment_ids = _flatten_array_with_offset(segment_ids, num_segments, n)

if num_inputs == 3:
    num_segments = None
else:
    num_segments *= n
output = op_func(data, indices, segment_ids, num_segments=num_segments)
output = _unflatten_first_dim(output, [n])
exit(wrap(output, True))
