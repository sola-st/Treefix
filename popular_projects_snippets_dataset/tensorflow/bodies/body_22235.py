# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Start threads for `QueueRunners`.

    Note that the queue runners collected in the graph key `QUEUE_RUNNERS`
    are already started automatically when you create a session with the
    supervisor, so unless you have non-collected queue runners to start
    you do not need to call this explicitly.

    Args:
      sess: A `Session`.
      queue_runners: A list of `QueueRunners`. If not specified, we'll use the
        list of queue runners gathered in the graph under the key
        `GraphKeys.QUEUE_RUNNERS`.

    Returns:
      The list of threads started for the `QueueRunners`.

    Raises:
      RuntimeError: If called with eager execution enabled.

    @compatibility(eager)
    Queues are not compatible with eager execution. To ingest data when eager
    execution is enabled, use the `tf.data` API.
    @end_compatibility
    """
if context.executing_eagerly():
    raise RuntimeError("Queues are not compatible with eager execution.")
if queue_runners is None:
    queue_runners = self._graph.get_collection(ops.GraphKeys.QUEUE_RUNNERS)
threads = []
for qr in queue_runners:
    threads.extend(
        qr.create_threads(sess, coord=self._coord, daemon=True, start=True))
exit(threads)
