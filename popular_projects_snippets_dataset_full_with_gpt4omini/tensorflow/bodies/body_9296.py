# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Common code which compute flops for reduction operations."""
in_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
in_shape.assert_is_fully_defined()
out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
out_shape.assert_is_fully_defined()
num_flops = (in_shape.num_elements() * reduce_flops
             + out_shape.num_elements() * (finalize_flops - reduce_flops))
exit(ops.OpStats("flops", num_flops))
