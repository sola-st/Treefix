# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Create a QueueRunner.

    On construction the `QueueRunner` adds an op to close the queue.  That op
    will be run if the enqueue ops raise exceptions.

    When you later call the `create_threads()` method, the `QueueRunner` will
    create one thread for each op in `enqueue_ops`.  Each thread will run its
    enqueue op in parallel with the other threads.  The enqueue ops do not have
    to all be the same op, but it is expected that they all enqueue tensors in
    `queue`.

    Args:
      queue: A `Queue`.
      enqueue_ops: List of enqueue ops to run in threads later.
      close_op: Op to close the queue. Pending enqueue ops are preserved.
      cancel_op: Op to close the queue and cancel pending enqueue ops.
      queue_closed_exception_types: Optional tuple of Exception types that
        indicate that the queue has been closed when raised during an enqueue
        operation.  Defaults to `(tf.errors.OutOfRangeError,)`.  Another common
        case includes `(tf.errors.OutOfRangeError, tf.errors.CancelledError)`,
        when some of the enqueue ops may dequeue from other Queues.
      queue_runner_def: Optional `QueueRunnerDef` protocol buffer. If specified,
        recreates the QueueRunner from its contents. `queue_runner_def` and the
        other arguments are mutually exclusive.
      import_scope: Optional `string`. Name scope to add. Only used when
        initializing from protocol buffer.

    Raises:
      ValueError: If both `queue_runner_def` and `queue` are both specified.
      ValueError: If `queue` or `enqueue_ops` are not provided when not
        restoring from `queue_runner_def`.
      RuntimeError: If eager execution is enabled.
    """
if context.executing_eagerly():
    raise RuntimeError(
        "QueueRunners are not supported when eager execution is enabled. "
        "Instead, please use tf.data to get data into your model.")

if queue_runner_def:
    if queue or enqueue_ops:
        raise ValueError("queue_runner_def and queue are mutually exclusive.")
    self._init_from_proto(queue_runner_def,
                          import_scope=import_scope)
else:
    self._init_from_args(
        queue=queue, enqueue_ops=enqueue_ops,
        close_op=close_op, cancel_op=cancel_op,
        queue_closed_exception_types=queue_closed_exception_types)
# Protect the count of runs to wait for.
self._lock = threading.Lock()
# A map from a session object to the number of outstanding queue runner
# threads for that session.
self._runs_per_session = weakref.WeakKeyDictionary()
# List of exceptions raised by the running threads.
self._exceptions_raised = []
