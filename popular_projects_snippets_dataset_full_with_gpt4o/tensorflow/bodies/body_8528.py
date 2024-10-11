# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Kill a server given task_type and task_id.

    Args:
      task_type: the type of the task such as "worker".
      task_id: the id the task such as 1.
    """
assert self._mpr
if (not self._start_events[task_type][task_id].is_set() or
    self._finish_events[task_type][task_id].is_set()):
    raise ValueError("The task %s:%d doesn't exist." % (task_type, task_id))

self._finish_events[task_type][task_id].set()
self._mpr._processes[(task_type, task_id)].join()
