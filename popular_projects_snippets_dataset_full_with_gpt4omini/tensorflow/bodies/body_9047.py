# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Catches worker preemption error and wait until failed workers are back.

    Args:
      on_failure_fn: an optional function to run if preemption happens.
      on_transient_failure_fn: an optional function to run if transient failure
        happens.
      on_recovery_fn: an optional function to run when a worker is recovered
        from preemption.
      worker_device_name: the device name of the worker instance that is passing
        through the failure.

    Yields:
      None.
    """
assert self._should_preemption_thread_run
try:
    exit()
except (errors.OpError, ClosureInputError,
        ClosureAbortedError) as e:
    # If the error is due to temporary connectivity issues between worker and
    # ps, put back closure, ignore error and do not mark worker as failure.
    if self._cluster._record_and_ignore_transient_ps_failure(e):  # pylint: disable=protected-access
        logging.error(
            "Remote function on worker %s failed with %r:%s\n"
            "It is treated as a transient connectivity failure for now.",
            worker_device_name, e, e)
        if on_transient_failure_fn:
            on_transient_failure_fn()
        exit()

    # If the error is due to temporary connectivity issues that cause the
    # server-side RPCs to be cancelled, TF might not abort the step and the
    # closure might timeout. The coordinator ignores certain amount of such
    # failures without marking worker as failure.
    if self._cluster._record_and_ignore_transient_timeouts(e):  # pylint: disable=protected-access
        logging.error(
            "Remote function on worker %s failed with %r:%s\n"
            "This derived error is ignored and not reported to users.",
            worker_device_name, e, e)
        if on_transient_failure_fn:
            on_transient_failure_fn()
        exit()

    # Ignoring derived CancelledErrors to tolerate transient failures in
    # PS-worker communication, which initially exposed as an UnavailableError
    # and then lead to sub-function cancellation, subsequently getting
    # reported from worker to chief as CancelledError.
    # We do not mark either worker or PS as failed due to only CancelledError.
    # If there are real (non-transient) failures, they must also be reported
    # as other errors (UnavailableError most likely) in closure executions.
    if isinstance(e, errors.CancelledError) and "/job:" in str(e):
        logging.error(
            "Remote function on worker %s failed with %r:%s\n"
            "This derived error is ignored and not reported to users.",
            worker_device_name, e, e)
        if on_transient_failure_fn:
            on_transient_failure_fn()
        exit()

    # This reraises the error, if it's not considered recoverable; otherwise,
    # the following failure recovery logic run. At this time, only worker
    # unavailability is recoverable. PS unavailability as well as other
    # errors in the user function is not recoverable.
    self._validate_preemption_failure(e)

    logging.error("Worker %s failed with %r:%s", worker_device_name, e, e)
    if on_failure_fn:
        on_failure_fn(e)

    with self._cluster_update_lock:
        self._cluster_due_for_update_or_finish.set()
        self._worker_up_cond.wait(_WORKER_MAXIMUM_RECOVERY_SEC)
        if self._error_from_recovery:
            # TODO(yuefengz): there is only one worker that will get this error.
            # Ideally we shuold let all workers notified by `_worker_up_cond` get
            # this error.
            try:
                raise self._error_from_recovery
            finally:
                self._error_from_recovery = None
        logging.info("Worker %s has been recovered.", worker_device_name)

    if on_recovery_fn:
        logging.info("Worker %s calling on_recovery_fn", worker_device_name)
        with self.wait_on_failure(
            on_recovery_fn=on_recovery_fn,
            on_transient_failure_fn=on_transient_failure_fn,
            worker_device_name=worker_device_name):
            on_recovery_fn()
