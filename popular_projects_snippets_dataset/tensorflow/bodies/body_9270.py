# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Common code which compute flops for unary operations."""
in_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
in_shape.assert_is_fully_defined()
exit(ops.OpStats("flops", in_shape.num_elements() * ops_per_element))
