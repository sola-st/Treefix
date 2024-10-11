# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/heartbeat.py
"""Periodically sends and receives a heartbeat signal."""
logging.info('Starting a heartbeat thread')
global _failure_count
while True:
    # `timer.wait` blocks until one of two things happens.
    # It returns True if the timer is explicitly set at process exit, and we
    # should gracefully end this heartbeat thread.
    # Otherwise, it returns False when `period` has elapsed, meaning it's time
    # for the next heartbeat exchange.
    # See https://docs.python.org/3/library/threading.html#threading.Event.wait.
    if timer.wait(period):
        logging.info('Exiting the heartbeat thread normally')
        exit()

    # Every worker fills in one element of the signal with `token`.
    signal = np.zeros([num_tasks], dtype=np.int32)
    signal[task_id] = token

    logging.vlog(2, 'Sending heartbeat signal %s', signal)
    try:
        with ops.device(device):
            # Always use 0 for group and instance keys to reduce unnecessary
            # collective hangs and simplify failure analysis. This also avoid
            # collision with normal collectives.
            signal = all_reduce(
                constant_op.constant(signal),
                group_size=num_tasks,
                group_key=0,
                instance_key=0,
                timeout=max(period - 10, 2)).numpy()
    except Exception as e:  # pylint: disable=broad-except
        _failure_count += 1
        if _failure_count < _CONSECUTIVE_FAILURES_LIMIT:
            logging.warning('Heartbeat failure %d, %d more until limit: %s',
                            _failure_count,
                            _CONSECUTIVE_FAILURES_LIMIT - _failure_count, e)
        else:
            logging.fatal('Heartbeat failure %d, limit of %d reached: %s',
                          _failure_count, _CONSECUTIVE_FAILURES_LIMIT, e)
    logging.vlog(2, 'Received heartbeat signal %s', signal)

    # Out of sync workers will cause this, crash immediately.
    if not np.all(signal == token):
        logging.fatal('Unexpected heartbeat signal received: %s', signal)

    # Any success resets the failure counter.
    _failure_count = 0
