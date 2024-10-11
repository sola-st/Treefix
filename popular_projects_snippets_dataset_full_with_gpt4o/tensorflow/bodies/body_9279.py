# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Compute flops for Softmax operation."""
# Softmax implemetation:
#
# Approximate flops breakdown:
#   2*n          -- compute shifted logits
#   n            -- exp of shifted logits
#   2*n          -- compute softmax from exp of shifted logits
exit(_unary_op_flops(graph, node, ops_per_element=5))
