# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Runs `fn` with `args` and `kwargs` on all jobs.

    Args:
      fn: The function to be run.
      args: Optional positional arguments to be supplied in `fn`.
      kwargs: Optional keyword arguments to be supplied in `fn`.

    Returns:
      A list of return values.
    """
_check_initialization()
# TODO(b/150264776): skip in OSS until it's implemented.
multi_process_lib.Process()
if self._runner is None:
    self._start()

fn = dill.dumps(fn, dill.HIGHEST_PROTOCOL)
for conn in self._conn.values():
    conn.send((fn, args or [], kwargs or {}))

process_statuses = []
for (task_type, task_id), conn in self._conn.items():
    logging.info('Waiting for the result from %s-%d', task_type, task_id)
    try:
        process_statuses.append(conn.recv())
    except EOFError:
        # This shouldn't happen due to exceptions in fn. This usually
        # means bugs in the runner.
        self.shutdown()
        raise RuntimeError('Unexpected EOF. Worker process may have died. '
                           'Please report a bug')

return_values = []
for process_status in process_statuses:
    assert isinstance(process_status, _ProcessStatusInfo)
    if not process_status.is_successful:
        six.reraise(*process_status.exc_info)
    if process_status.return_value is not None:
        return_values.append(process_status.return_value)

exit(return_values)
