# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
self._snapshots = []
# cache the function used by mark_stack_trace_and_call to avoid
# contaminating the leak measurement.
def _record_snapshot():
    self._snapshots.append(_create_python_object_snapshot())

self._record_snapshot = _record_snapshot
