# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
StopCoordinatorWithException.after_run(self, run_context, run_values)
try:
    # After a `run`, an exception could have been stored inside the
    # coordinator.
    self._coord.raise_requested_exception()
except errors_impl.AbortedError:
    # In real world, the main thread may or may not know about the exception
    # that stopped the coordinator. Because the coordinator has stopped, the
    # main thread could have gotten stuck as well (for example, the
    # coordinator was supposed to execute `FIFOQueue.enqueue` while the main
    # thread is executing a blocking `FIFOQueue.dequeue`). After it got stuck,
    # the session is going to get garbage collected after some time with:
    raise errors_impl.CancelledError(None, None,
                                     'Session got garbage-collected.')
