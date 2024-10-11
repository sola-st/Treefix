# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
stack_size = pfor_input.pfor.loop_len_vector[0]
input_sizes = pfor_input.unstacked_input(0)
data_format = pfor_input.get_attr("data_format")
c_dim = 1 if data_format == b"NCHW" else 3
input_sizes_mutipliers = [
    constant_op.constant([1] * c_dim, dtype=dtypes.int32), [stack_size]
]
if c_dim < 3:
    input_sizes_mutipliers += [
        constant_op.constant([1] * (3 - c_dim), dtype=dtypes.int32)
    ]
input_sizes *= array_ops.concat(input_sizes_mutipliers, axis=0)
kernel = _flatten_with_inner_dim(pfor_input.stacked_input(1), 3, 5)
out_backprop = _flatten_with_inner_dim(
    pfor_input.stacked_input(2), c_dim + 1, 5)
result = _create_op(
    "DepthwiseConv2dNativeBackpropInput", [input_sizes, kernel, out_backprop],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs[0]
exit(wrap(_unflatten_with_inner_dim(result, c_dim, 4, stack_size), True))
