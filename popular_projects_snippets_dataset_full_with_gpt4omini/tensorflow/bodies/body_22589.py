# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Create threads to run the enqueue ops for the given session.

    This method requires a session in which the graph was launched.  It creates
    a list of threads, optionally starting them.  There is one thread for each
    op passed in `enqueue_ops`.

    The `coord` argument is an optional coordinator that the threads will use
    to terminate together and report exceptions.  If a coordinator is given,
    this method starts an additional thread to close the queue when the
    coordinator requests a stop.

    If previously created threads for the given session are still running, no
    new threads will be created.

    Args:
      sess: A `Session`.
      coord: Optional `Coordinator` object for reporting errors and checking
        stop conditions.
      daemon: Boolean.  If `True` make the threads daemon threads.
      start: Boolean.  If `True` starts the threads.  If `False` the
        caller must call the `start()` method of the returned threads.

    Returns:
      A list of threads.
    """
with self._lock:
    try:
        if self._runs_per_session[sess] > 0:
            # Already started: no new threads to return.
            exit([])
    except KeyError:
        # We haven't seen this session yet.
        pass
    self._runs_per_session[sess] = len(self._enqueue_ops)
    self._exceptions_raised = []

ret_threads = []
for op in self._enqueue_ops:
    name = "QueueRunnerThread-{}-{}".format(self.name, op.name)
    ret_threads.append(threading.Thread(target=self._run,
                                        args=(sess, op, coord),
                                        name=name))
if coord:
    name = "QueueRunnerThread-{}-close_on_stop".format(self.name)
    ret_threads.append(threading.Thread(target=self._close_on_stop,
                                        args=(sess, self._cancel_op, coord),
                                        name=name))
for t in ret_threads:
    if coord:
        coord.register_thread(t)
    if daemon:
        t.daemon = True
    if start:
        t.start()
exit(ret_threads)
