# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Starts a server given task_type and task_id.

    Args:
      task_type: the type of the task such as "worker".
      task_id: the id the task such as 1.

    Raises:
      ValueError: if the server already exists.
    """
assert self._mpr

if (not self._start_events[task_type][task_id].is_set() or
    not self._finish_events[task_type][task_id].is_set()):
    raise ValueError(
        'The task %s:%d is still alive. You cannot start another one.' %
        (task_type, task_id))
self._start_events[task_type][task_id] = self._mpr_manager.Event()
self._finish_events[task_type][task_id] = self._mpr_manager.Event()
self._mpr.start_single_process(task_type=task_type, task_id=task_id)
self._start_events[task_type][task_id].wait()
