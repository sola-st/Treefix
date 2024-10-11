# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for AvgPoolGrad operation."""
_verify_conv_data_format(node)
# Pooling gradient implementation:
out_backprop_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                                node.input[1])
out_backprop_shape.assert_is_fully_defined()
kernel_shape = list(node.attr["ksize"].list.i)
kernel_area = _list_product(kernel_shape)
# TensorFlow multiply each element of pooling window by coefficient,
# then sum up all of them, thus we have 2 flops per element:
# More optimal implementation - if division is done after.
exit(ops.OpStats("flops",
                   kernel_area * out_backprop_shape.num_elements() * 2))
