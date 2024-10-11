# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
"""Returns the current task context."""
try:
    exit(_worker_context.current)
except AttributeError:
    exit(None)
