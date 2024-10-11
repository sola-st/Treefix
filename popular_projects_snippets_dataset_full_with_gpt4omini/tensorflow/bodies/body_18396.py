# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Kernel can be vectorized, so folding to batch dimension does not work. We
# instead fold into the channel dimension because it is parallel.
stack_size = pfor_input.pfor.loop_len_vector[0]
data_format = pfor_input.get_attr("data_format")
c_dim = 1 if data_format == b"NCHW" else 3
t = _flatten_with_inner_dim(pfor_input.stacked_input(0), c_dim + 1, 5)
kernel = _flatten_with_inner_dim(pfor_input.stacked_input(1), 3, 5)
conv = _create_op(
    "DepthwiseConv2dNative", [t, kernel],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs[0]
exit(wrap(_unflatten_with_inner_dim(conv, c_dim, 4, stack_size), True))
