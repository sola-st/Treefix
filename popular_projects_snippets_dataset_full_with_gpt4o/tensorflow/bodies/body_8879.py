# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
"""Asserts `second_fn` wouldn't return before `first_fn` is finished."""
first_fn_done = threading.Event()
second_fn_done = threading.Event()
coord = coordinator.Coordinator(clean_stop_exception_types=[])

def wrapped_first_fn():
    with coord.stop_on_exception():
        self.assertFalse(second_fn_done.is_set())
        first_fn()
        first_fn_done.set()

self.assertFalse(first_fn_done.is_set())
t = threading.Thread(target=wrapped_first_fn)
t.start()

second_fn()
self.assertTrue(first_fn_done.is_set())
second_fn_done.set()

coord.join([t])
