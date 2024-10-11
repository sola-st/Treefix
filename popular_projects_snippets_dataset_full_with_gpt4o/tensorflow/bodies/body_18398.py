# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
stack_size = pfor_input.pfor.loop_len_vector[0]
data_format = pfor_input.get_attr("data_format")
c_dim = 1 if data_format == b"NCHW" else 3
inputs = _flatten_with_inner_dim(pfor_input.stacked_input(0), c_dim + 1, 5)
filter_sizes = pfor_input.unstacked_input(1)
filter_sizes_multipliers = [
    constant_op.constant([1, 1], dtype=dtypes.int32), [stack_size],
    constant_op.constant([1], dtype=dtypes.int32)
]
filter_sizes *= array_ops.concat(filter_sizes_multipliers, axis=0)
out_backprop = _flatten_with_inner_dim(
    pfor_input.stacked_input(2), c_dim + 1, 5)
result = _create_op(
    "DepthwiseConv2dNativeBackpropFilter",
    [inputs, filter_sizes, out_backprop],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs[0]
exit(wrap(_unflatten_with_inner_dim(result, 2, 4, stack_size), True))
