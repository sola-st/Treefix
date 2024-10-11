# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Ensure the worker preemption thread is closed."""
self._should_preemption_thread_run = False
with self._cluster_update_lock:
    self._cluster_due_for_update_or_finish.set()
