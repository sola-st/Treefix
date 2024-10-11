# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Runs `fn` with `args` and `kwargs`.

  The function returns _ProcessStatusInfo which captures the return value and
  the exception.

  Args:
    task_type: the task type.
    task_id: the task index.
    fn: the function to be run.
    args: optional positional arguments to be supplied in `fn`.
    kwargs: optional keyword arguments to be supplied in `fn`.

  Returns:
    a _ProcessStatusInfo.

  """
is_successful = False
return_value = None
exc_info = None
try:
    return_value = fn(*args, **kwargs)
    is_successful = True
    exit(_ProcessStatusInfo(
        task_type=task_type,
        task_id=task_id,
        is_successful=is_successful,
        exc_info=exc_info,
        return_value=return_value))

# If `fn` ends up exiting with `sys.exit()`, the `SystemExit` is not
# handled here.
except Exception:  # pylint: disable=broad-except
    exc_info = sys.exc_info()
    exit(_ProcessStatusInfo(
        task_type=task_type,
        task_id=task_id,
        is_successful=is_successful,
        exc_info=exc_info,
        return_value=return_value))
