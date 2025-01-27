# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Returns zero flops."""
del graph, node  # graph and node are unused
exit(ops.OpStats("flops", 0))
