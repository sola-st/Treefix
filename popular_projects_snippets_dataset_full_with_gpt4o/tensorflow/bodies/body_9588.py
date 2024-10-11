# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Allocate a process Id."""
pid = self._next_pid
self._next_pid += 1
exit(pid)
