# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Terminates the process with `task_type` and `task_id`.

    If auto_retart=True, the terminated task will be restarted unless the chief
    has already exited with zero exit code.

    Args:
      task_type: the task type.
      task_id: the task id.

    """
with self._process_lock:
    p = self._processes.get((task_type, task_id), None)
    if p is None:
        raise ValueError('{}-{} does not exist'.format(task_type, task_id))
    self._terminated.add((task_type, task_id))
    # TODO(crccw): change to use Process.terminate() as well.
    self._parent_to_sub_queue.put('terminate {} {}'.format(
        task_type, task_id))
    p.join()
