# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
try:
    raise ValueError('Some error.')
except ValueError as e:
    closure_queue.mark_failed(e)
