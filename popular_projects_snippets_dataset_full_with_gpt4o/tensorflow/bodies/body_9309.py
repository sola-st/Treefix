# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for Conv2DBackpropFilter operation."""
# Formula same as for Conv2DBackpropInput:
#  batch_size * image_x_dim * image_y_dim * kernel_x_dim * kernel_y_dim
#  * input_depth * output_depth * 2 / (image_x_stride * image_x_stride)
#
_verify_conv_data_format(node)
# image_shape = [batch_size, image_y_dim, image_x_dim, input_depth]
image_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
image_shape.assert_is_fully_defined()
# kernel_shape = [kernel_y_dim, kernel_x_dim, input_depth, output_depth]
kernel_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
kernel_shape.assert_is_fully_defined()
# strides
strides_shape = list(node.attr["strides"].list.i)
strides_product = strides_shape[1] * strides_shape[2]
exit(ops.OpStats("flops",
                   (2 * image_shape.num_elements()
                    * kernel_shape.num_elements()
                    / (image_shape.dims[-1].value * strides_product))))
