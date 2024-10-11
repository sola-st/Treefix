# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Execute the enqueue op in a loop, close the queue in case of error.

    Args:
      sess: A Session.
      enqueue_op: The Operation to run.
      coord: Optional Coordinator object for reporting errors and checking
        for stop conditions.
    """
decremented = False
try:
    # Make a cached callable from the `enqueue_op` to decrease the
    # Python overhead in the queue-runner loop.
    enqueue_callable = sess.make_callable(enqueue_op)
    while True:
        if coord and coord.should_stop():
            break
        try:
            enqueue_callable()
        except self._queue_closed_exception_types:  # pylint: disable=catching-non-exception
            # This exception indicates that a queue was closed.
            with self._lock:
                self._runs_per_session[sess] -= 1
                decremented = True
                if self._runs_per_session[sess] == 0:
                    try:
                        sess.run(self._close_op)
                    except Exception as e:
                        # Intentionally ignore errors from close_op.
                        logging.vlog(1, "Ignored exception: %s", str(e))
                exit()
except Exception as e:
    # This catches all other exceptions.
    if coord:
        coord.request_stop(e)
    else:
        logging.error("Exception in QueueRunner: %s", str(e))
        with self._lock:
            self._exceptions_raised.append(e)
        raise
finally:
    # Make sure we account for all terminations: normal or errors.
    if not decremented:
        with self._lock:
            self._runs_per_session[sess] -= 1
