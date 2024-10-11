# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Run tasks in a thread.

    If `tf_config` is provided, use it for the new thread; if not, construct one
    from `cluster_spec`, `task_type`, and `task_id`, and provide it to the new
    thread to be set as `TF_CONFIG` environment.

    Args:
      task_fn: The function to run in the new thread.
      cluster_spec: The cluster spec.
      task_type: The task type.
      task_id: The task id.
      *args: Additional positional arguments to provide to the thread's task_fn.
      **kwargs: Additional keyword arguments to provide to the thread's task_fn.
        If `tf_config` is provided, that dict will be used for the TF_CONFIG for
        the new thread.

    Returns:
      The thread that has started.
    """
tf_config = kwargs.pop('tf_config', None)
if tf_config is None:
    if task_type:
        tf_config = {
            'cluster': cluster_spec,
            'task': {
                'type': task_type,
                'index': task_id
            }
        }
    else:
        tf_config = {
            'cluster': cluster_spec,
        }
t = threading.Thread(
    target=self._task_thread,
    args=(task_fn, tf_config, context.executing_eagerly()) + args,
    kwargs=kwargs)
t.start()
exit(t)
