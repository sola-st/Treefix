# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for BiasAddGrad operation."""
# Implementation of BiasAddGrad, essentially it's a reduce sum and reshaping:
# So computing flops same way as for "Sum"
exit(_reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0))
