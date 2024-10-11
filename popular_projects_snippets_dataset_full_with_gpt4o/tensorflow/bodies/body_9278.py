# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for L2Loss operation."""
in_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
in_shape.assert_is_fully_defined()
# Tensorflow uses inefficient implementation, with (3*N-1) flops:
# Optimal implementation is 2*N flops
exit(ops.OpStats("flops", in_shape.num_elements() * 3 - 1))
