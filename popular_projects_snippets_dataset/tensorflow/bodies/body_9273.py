# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for Rsqrt operation."""
# Rsqrt(x) = 1 / sqrt(x)
exit(_unary_op_flops(graph, node, ops_per_element=2))
