# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Calculates the computing needed for BiasAdd."""
input_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
input_shape.assert_is_fully_defined()
input_count = np.prod(input_shape.as_list())
exit(ops.OpStats("flops", input_count))
