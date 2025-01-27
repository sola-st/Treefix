# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Waits until all other callers reach the same wait call."""
self._local_sense.value = not self._flag
with self._lock:
    self._counter += 1
    if self._counter == self._num_participants:
        self._counter = 0
        self._flag = self._local_sense.value
with self._condition:
    while self._flag != self._local_sense.value:
        self._condition.wait()
    self._condition.notify_all()
