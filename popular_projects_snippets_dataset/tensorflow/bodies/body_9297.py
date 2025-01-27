# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for Mean operation."""
# reduction - sum, finalization - divide
exit(_reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=1))
