# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
with coord.stop_on_exception():
    self.assertFalse(second_fn_done.is_set())
    first_fn()
    first_fn_done.set()
