# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Returns a context manager for a managed session.

    This context manager creates and automatically recovers a session.  It
    optionally starts the standard services that handle checkpoints and
    summaries.  It monitors exceptions raised from the `with` block or from the
    services and stops the supervisor as needed.

    The context manager is typically used as follows:

    ```python
    def train():
      sv = tf.compat.v1.train.Supervisor(...)
      with sv.managed_session(<master>) as sess:
        for step in range(..):
          if sv.should_stop():
            break
          sess.run(<my training op>)
          ...do other things needed at each training step...
    ```

    An exception raised from the `with` block or one of the service threads is
    raised again when the block exits.  This is done after stopping all threads
    and closing the session.  For example, an `AbortedError` exception, raised
    in case of preemption of one of the workers in a distributed model, is
    raised again when the block exits.

    If you want to retry the training loop in case of preemption you can do it
    as follows:

    ```python
    def main(...):
      while True
        try:
          train()
        except tf.errors.Aborted:
          pass
    ```

    As a special case, exceptions used for control flow, such as
    `OutOfRangeError` which reports that input queues are exhausted, are not
    raised again from the `with` block: they indicate a clean termination of
    the training loop and are considered normal termination.

    Args:
      master: name of the TensorFlow master to use.  See the
        `tf.compat.v1.Session` constructor for how this is interpreted.
      config: Optional `ConfigProto` proto used to configure the session. Passed
        as-is to create the session.
      start_standard_services: Whether to start the standard services, such as
        checkpoint, summary and step counter.
      close_summary_writer: Whether to close the summary writer when closing the
        session.  Defaults to True.

    Returns:
      A context manager that yields a `Session` restored from the latest
      checkpoint or initialized from scratch if not checkpoint exists.  The
      session is closed when the `with` block exits.
    """
try:
    sess = self.prepare_or_wait_for_session(
        master=master,
        config=config,
        start_standard_services=start_standard_services)
    exit(sess)
except Exception as e:
    self.request_stop(e)
finally:
    try:
        # Request all the threads to stop and wait for them to do so.  Any
        # exception raised by the threads is raised again from stop().
        # Passing stop_grace_period_secs is for blocked enqueue/dequeue
        # threads which are not checking for `should_stop()`.  They
        # will be stopped when we close the session further down.
        self.stop(close_summary_writer=close_summary_writer)
    finally:
        # Close the session to finish up all pending calls.  We do not care
        # about exceptions raised when closing.  This takes care of
        # blocked enqueue/dequeue calls.
        try:
            sess.close()
        except Exception:
            # Silently ignore exceptions raised by close().
            pass
