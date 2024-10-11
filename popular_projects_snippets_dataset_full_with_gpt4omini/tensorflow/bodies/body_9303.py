# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Common code which compute flops for pooling operations."""
# compute flops for average and max pooling
_verify_conv_data_format(node)
#
# Pooling declaration:
#   Inputs:
#     - value
#   Outputs:
#     - output
#   Attributes:
#     - ksize
#     - strides
#     - padding
#     - data_format
#
# Pooling implemetation:
out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
out_shape.assert_is_fully_defined()
kernel_shape = list(node.attr["ksize"].list.i)
kernel_area = _list_product(kernel_shape)
exit(ops.OpStats("flops", kernel_area * out_shape.num_elements()))
