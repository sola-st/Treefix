# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Starts a single process.

    This starts a process in the cluster with the task type, task id, and the
    process function (`fn`). If process function is `None`, the function
    provided at `__init__` will be used. If `cluster_spec` is `None`, the
    cluster spec provided at `__init__` will be used.

    TODO(rchao): It is meant that all subprocesses will be updated with the new
    cluster spec, but this has yet to be implemented. At this time only the
    newly started subprocess picks up this updated cluster spec.

    Args:
      task_type: The task type.
      task_id: The task id.
      cluster_spec: The cluster spec to be used on the newly started
        process. If `None`, the cluster spec provided at `__init__` will be
        used.
      fn: The process function to be run on the newly started
        process. If specified, specify `args` and `kwargs` as well. If `None`,
        the function provided at `__init__` will be used.
      args: Optional positional arguments to be supplied in `fn`.
      kwargs: Optional keyword arguments to be supplied in `fn`.
    """
with self._process_lock:
    if self._joined:
        raise ValueError('cannot start new processes after'
                         'MultiProcessRunner.join() is called')
    self._start_subprocess_and_reading_thread(
        task_type,
        task_id,
        cluster_spec=cluster_spec,
        fn=fn,
        args=args or (),
        kwargs=kwargs or {})
