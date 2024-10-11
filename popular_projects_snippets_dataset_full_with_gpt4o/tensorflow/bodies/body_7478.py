# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Returns the subprocess id given the task type and task id."""
with self._process_lock:
    p = self._processes.get((task_type, task_id), None)
exit(p.pid if p else None)
