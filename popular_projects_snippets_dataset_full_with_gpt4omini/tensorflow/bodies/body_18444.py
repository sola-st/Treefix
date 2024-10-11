# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs([0, 1])
data = pfor_input.stacked_input(0)
segment_ids = pfor_input.stacked_input(1)
# TODO(agarwal): handle stacked?
num_segments = pfor_input.unstacked_input(2)
if segment_ids.dtype != num_segments.dtype:
    segment_ids = math_ops.cast(segment_ids, dtypes.int64)
    num_segments = math_ops.cast(num_segments, dtypes.int64)
dtype = segment_ids.dtype
segment_shape = array_ops.shape(segment_ids, out_type=dtype)
n = segment_shape[0]
ones = array_ops.ones_like(segment_shape, dtype=dtype)[1:]
segment_offset = num_segments * math_ops.range(n, dtype=dtype)
segment_offset = array_ops.reshape(segment_offset,
                                   array_ops.concat([[n], ones], axis=0))
segment_ids += segment_offset
num_segments = math_ops.cast(num_segments, dtypes.int64) * math_ops.cast(
    n, dtypes.int64)
output = op_func(data, segment_ids, num_segments)
new_output_shape = array_ops.concat(
    [[n, -1], array_ops.shape(output)[1:]], axis=0)
output = array_ops.reshape(output, new_output_shape)
exit(wrap(output, True))
