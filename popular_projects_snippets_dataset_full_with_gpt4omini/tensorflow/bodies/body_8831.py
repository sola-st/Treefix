# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
"""Ensures worker and preemption threads are closed."""
# Worker and preemption threads should exist before releasing
# ClusterCoordinator.
running_threads = test_util.get_running_threads()
self.assertTrue(
    test_util.has_thread(_WORKER_THREAD_PREFIX, running_threads))
self.assertIn(_WORKER_PREEMPTION_THREAD_NAME, running_threads)

# Print object graph if ClusterCoordinator may leak.
if sys.getrefcount(self.cluster_coord) > 2:
    try:
        test_util.show_backref(self.cluster_coord)
    except:  # pylint: disable=bare-except
        pass

    # Wait for threads to close.
self.cluster_coord = None
self.strategy = None
gc.collect()
time.sleep(1)

# Verify thread names.
running_threads = test_util.get_running_threads()
self.assertNotIn(_WORKER_PREEMPTION_THREAD_NAME, running_threads)
self.assertFalse(
    test_util.has_thread(_WORKER_THREAD_PREFIX, running_threads),
    "Worker thread is not stopped properly.")
