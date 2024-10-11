# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for AddN operation."""
if not node.input:
    exit(_zero_flops(graph, node))
in_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
in_shape.assert_is_fully_defined()
exit(ops.OpStats("flops", in_shape.num_elements() * (len(node.input) - 1)))
