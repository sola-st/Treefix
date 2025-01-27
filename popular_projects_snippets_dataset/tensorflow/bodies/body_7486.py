# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Terminates all subprocesses.

    The caller is required to hold self._process_lock.

    Args:
      sig: the signal used to terminate the process. The default is SIGKILL.
    """

# Use SIGKILL as default. In systems where that's unavailable such as
# windows, use SIGTERM.
sig = sig or getattr(signal, 'SIGKILL', signal.SIGTERM)
for (task_type, task_id), p in self._processes.items():
    if p.exitcode is not None:
        logging.info('%s-%d has already exited. Not terminating.', task_type,
                     task_id)
        continue
    try:
        os.kill(p.pid, sig)
        self._terminated.add((task_type, task_id))
        logging.info('%s-%d terminated with signal %r.', task_type, task_id,
                     sig)
    except ProcessLookupError:
        logging.info('Attempting to kill %s-%d but it does not exist.',
                     task_type, task_id)
