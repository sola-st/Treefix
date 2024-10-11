# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Terminates all subprocesses."""
with self._process_lock:
    self._terminate_all(sig)
