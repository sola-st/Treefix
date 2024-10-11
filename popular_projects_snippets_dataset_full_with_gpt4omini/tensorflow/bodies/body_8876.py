# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
with coord.stop_on_exception():
    closure_queue.get()
    closure_queue.mark_finished()
