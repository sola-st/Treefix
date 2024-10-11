# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for MaxPoolGrad operation."""
_verify_conv_data_format(node)
#
# MaxPoolGrad declaration:
#   Inputs:
#     - orig_input  -- original input tensor (of max_pool)
#     - orig_output  -- original output tensor (of max_pool)
#     - grad --  gradient with respect to output of max_pool
#   Outputs:
#     - output -- gradient with respect to input of max_pool
#   Attributes:
#     - ksize
#     - strides
#     - padding
#     - data_format
# It computes MaxPool first, then one flop per each element of original output
#
kernel_shape = list(node.attr["ksize"].list.i)
kernel_area = _list_product(kernel_shape)
orig_out_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                            node.input[1])
orig_out_shape.assert_is_fully_defined()
max_pool_ops = kernel_area * orig_out_shape.num_elements()
exit(ops.OpStats("flops", max_pool_ops + orig_out_shape.num_elements()))
