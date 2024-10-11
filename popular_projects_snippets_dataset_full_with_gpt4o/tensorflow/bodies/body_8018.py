# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Returns whether a worker context has been entered."""
exit(dc_context.get_current_worker_context() is not None)
