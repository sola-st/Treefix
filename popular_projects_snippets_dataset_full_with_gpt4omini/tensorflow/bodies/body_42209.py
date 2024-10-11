# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""A context manager to allow setting the mode to EAGER/GRAPH."""
ctx = self._thread_local_data
old_is_eager = ctx.is_eager
ctx.is_eager = mode == EAGER_MODE
if mode == EAGER_MODE:
    # Entering graph mode does not provide us with sufficient information to
    # record a context switch; graph-based context switches are only logged
    # when a graph is registered as the default graph.
    self.context_switches.push(False, eager_mode, None)
try:
    exit()
finally:
    ctx.is_eager = old_is_eager
    if mode == EAGER_MODE:
        self.context_switches.pop()
