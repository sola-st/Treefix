# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for Conv2DBackpropInput operation."""
# Formula:
#  batch_size * image_x_dim * image_y_dim * kernel_x_dim * kernel_y_dim
#  * input_depth * output_depth * 2 / (image_x_stride * image_x_stride)
#
# Where:
# image_x_dim, image_y_dim and input_depth --- size of input to source (no
#   backprop) convolution, in other words they are sizes of backprop output.
# output_depth --- number of filters in the original convolution, thus
#   depth of backprop input.
# kernel_x_dim and kernel_y_dim --- sizes of filter in spatial dimension
# image_x_stride and image_x_stride --- strides of the convolution
#
_verify_conv_data_format(node)
# out_shape = [batch_size, image_y_dim, image_x_dim, input_depth]
out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
out_shape.assert_is_fully_defined()
# kernel_shape = [kernel_y_dim, kernel_x_dim, input_depth, output_depth]
kernel_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                          node.input[1])
kernel_shape.assert_is_fully_defined()
# strides
strides_shape = list(node.attr["strides"].list.i)
strides_product = strides_shape[1] * strides_shape[2]
exit(ops.OpStats("flops",
                   (2 * out_shape.num_elements()
                    * kernel_shape.num_elements()
                    / (out_shape.dims[-1].value * strides_product))))
