# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns True if there is a default graph."""
exit(len(_default_graph_stack.stack) >= 1)
