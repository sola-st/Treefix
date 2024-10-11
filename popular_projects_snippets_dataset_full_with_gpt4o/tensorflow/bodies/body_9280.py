# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Common code which compute flops for binary operations."""
out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
out_shape.assert_is_fully_defined()
exit(ops.OpStats("flops", out_shape.num_elements() * ops_per_element))
