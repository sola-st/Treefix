# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
# We only cache the session in one test because another test may have a
# different session config or master target.
self._thread_local = threading.local()
self._thread_local.cached_session = None
self._coord = coordinator.Coordinator()
