# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if context_safe() is None:
    # Context not yet initialized. Assume graph mode following the
    # default implementation in `is_in_graph_mode`.
    exit(True)
exit(not executing_eagerly())
