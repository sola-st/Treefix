# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Starts all queue runners collected in the graph.

  This is a companion method to `add_queue_runner()`.  It just starts
  threads for all queue runners collected in the graph.  It returns
  the list of all threads.

  @compatibility(TF2)
  QueueRunners are not compatible with eager execution. Instead, please
  use [tf.data](https://www.tensorflow.org/guide/data) to get data into your
  model.
  @end_compatibility

  Args:
    sess: `Session` used to run the queue ops.  Defaults to the
      default session.
    coord: Optional `Coordinator` for coordinating the started threads.
    daemon: Whether the threads should be marked as `daemons`, meaning
      they don't block program exit.
    start: Set to `False` to only create the threads, not start them.
    collection: A `GraphKey` specifying the graph collection to
      get the queue runners from.  Defaults to `GraphKeys.QUEUE_RUNNERS`.

  Raises:
    ValueError: if `sess` is None and there isn't any default session.
    TypeError: if `sess` is not a `tf.compat.v1.Session` object.

  Returns:
    A list of threads.

  Raises:
    RuntimeError: If called with eager execution enabled.
    ValueError: If called without a default `tf.compat.v1.Session` registered.
  """
if context.executing_eagerly():
    raise RuntimeError("Queues are not compatible with eager execution.")
if sess is None:
    sess = ops.get_default_session()
    if not sess:
        raise ValueError("Cannot start queue runners: No default session is "
                         "registered. Use `with sess.as_default()` or pass an "
                         "explicit session to tf.start_queue_runners(sess=sess)")

if not isinstance(sess, session.SessionInterface):
    # Following check is due to backward compatibility. (b/62061352)
    if sess.__class__.__name__ in [
        "MonitoredSession", "SingularMonitoredSession"]:
        exit([])
    raise TypeError("sess must be a `tf.Session` object. "
                    "Given class: {}".format(sess.__class__))

queue_runners = ops.get_collection(collection)
if not queue_runners:
    logging.warning(
        "`tf.train.start_queue_runners()` was called when no queue runners "
        "were defined. You can safely remove the call to this deprecated "
        "function.")

with sess.graph.as_default():
    threads = []
    for qr in ops.get_collection(collection):
        threads.extend(qr.create_threads(sess, coord=coord, daemon=daemon,
                                         start=start))
exit(threads)
