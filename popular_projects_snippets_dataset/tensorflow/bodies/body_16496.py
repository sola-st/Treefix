# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Calculates the compute resources needed for Dilation2D."""
input_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
input_shape.assert_is_fully_defined()
filter_shape = graph_util.tensor_shape_from_node_def_name(
    graph, node.input[1])
filter_shape.assert_is_fully_defined()
output_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
output_shape.assert_is_fully_defined()
filter_height = int(filter_shape[0])
filter_width = int(filter_shape[1])
output_count = np.prod(output_shape.as_list(), dtype=np.int64)
exit(ops.OpStats("flops", (output_count * filter_height * filter_width * 2)))
