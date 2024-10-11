# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_context.py
"""Returns the current task context."""
try:
    exit(_worker_context.current)
except AttributeError:
    exit(None)
