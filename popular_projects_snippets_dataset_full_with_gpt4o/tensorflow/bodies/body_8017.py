# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Waits for other workers to reach the same call to this method."""
exit(dc_context.get_current_worker_context().wait_for_other_workers())
