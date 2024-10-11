# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
try:
    raise error
except Exception as e:  # pylint: disable=broad-except
    closure.output_remote_value._set_error(e)
    closure_queue.mark_failed(e)
