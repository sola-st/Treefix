# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Joins all the processes with timeout.

    If any of the subprocesses does not exit approximately after `timeout`
    seconds has passed after `join` call, this raises a
    `SubprocessTimeoutError`.

    Note: At timeout, it uses SIGTERM to terminate the subprocesses, in order to
    log the stack traces of the subprocesses when they exit. However, this
    results in timeout when the test runs with tsan (thread sanitizer); if tsan
    is being run on the test targets that rely on timeout to assert information,
    `MultiProcessRunner.terminate_all()` must be called after `join()`, before
    the test exits, so the subprocesses are terminated with SIGKILL, and data
    race is removed.

    Args:
      timeout: optional integer or `None`. If provided as an integer, and not
      all processes report status within roughly `timeout` seconds, a
      `SubprocessTimeoutError` exception will be raised. If `None`, `join` never
      times out.

    Returns:
      A `MultiProcessRunnerResult` object, which has two attributes,
      `return_value` and `stdout`. `return_value` always contains a list of
      return values from the subprocesses, although the order is not meaningful.
      If `return_output` argument is True at `__init__`, `stdout` is available
      that contains a list of all messages from subprocesses' stdout and stderr.

    Raises:
      SubprocessTimeoutError: if not all processes report status approximately
        within `timeout` seconds. When this is raised, a
        `MultiProcessRunnerResult` object can be retrieved by
        `SubprocessTimeoutError`'s mpr_result attribute, which has the same
        structure as above 'Returns' section describes.
      UnexpectedSubprocessExitError: If any of the subprocesses did not exit
        properly (for example, they exit on SIGTERM or SIGKILL signal). When
        this is raised, a `MultiProcessRunnerResult` object can be retrieved by
        `UnexpectedSubprocessExitError`'s mpr_result attribute, which has the
        same structure as above 'Returns' section describes. If `max_run_time`
        is not `None`, it is expected that some subprocesses may be
        force-killed when `max_run_time` is up, and this is raised in those
        cases.
      Exception: if there is an Exception propagated from any subprocess. When
        this is raised, a `MultiProcessRunnerResult` object can be retrieved by
        `UnexpectedSubprocessExitError`'s mpr_result attribute, which has the
        same structure as above 'Returns' section describes.
    """
if timeout and not isinstance(timeout, int):
    raise ValueError('`timeout` must be an integer or `None`.')
with self._process_lock:
    if self._joined:
        raise ValueError("MultiProcessRunner can't be joined twice.")
    self._joined = True

self._watchdog_thread.join(timeout)
if self._watchdog_thread.is_alive():
    # Timeout. Force termination to dump worker processes stack trace.
    with self._process_lock:
        self._auto_restart = False
    logging.error('Timeout when joining for child processes. Terminating...')
    self.terminate_all(sig=signal.SIGTERM)
    # Wait for the processes to terminate by themselves first, so they have a
    # chance to dump stacktraces. After _FORCE_KILL_WAIT_SEC, we SIGKILL them.
    self._watchdog_thread.join(_FORCE_KILL_WAIT_SEC)
    if self._watchdog_thread.is_alive():
        logging.error('Timeout when waiting for child processes to '
                      'print stacktrace. Sending SIGKILL...')
        self.terminate_all()
        self._watchdog_thread.join()
    process_statuses = self._get_process_statuses()
    self._reraise_if_subprocess_error(process_statuses)
    raise SubprocessTimeoutError(
        'One or more subprocesses timed out, where timeout was set to {}s. '
        'Please change the `timeout` argument for '
        '`MultiProcessRunner.join()` or `multi_process_runner.run()` '
        'if it should be adjusted.'.format(timeout),
        self._get_mpr_result(process_statuses))

for (task_type, task_id), p in self._processes.items():
    logging.info('%s-%d exit code: %s', task_type, task_id, p.exitcode)

process_statuses = self._get_process_statuses()
self._reraise_if_subprocess_error(process_statuses)

# Checking all the processes that are expected to exit properly.
for (task_type, task_id), p in self._processes.items():
    # Successfully exiting process has exit code 0. We ignore processes that
    # are terminated.
    assert p.exitcode is not None
    if (p.exitcode > 0 and (task_type, task_id) not in self._terminated):
        raise UnexpectedSubprocessExitError(
            'Subprocess %s-%d exited with exit code %s. See logs for details.'
            % (task_type, task_id, p.exitcode),
            self._get_mpr_result(process_statuses))

logging.info('Joining log reading threads.')
for thread in self._reading_threads:
    thread.join()
logging.info('Joined log reading threads.')

# Clear the alarm.
signal.alarm(0)

exit(self._get_mpr_result(process_statuses))
