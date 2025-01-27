# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Creates a `FileWriter`, optionally shared within the given session.

    Typically, constructing a file writer creates a new event file in `logdir`.
    This event file will contain `Event` protocol buffers constructed when you
    call one of the following functions: `add_summary()`, `add_session_log()`,
    `add_event()`, or `add_graph()`.

    If you pass a `Graph` to the constructor it is added to
    the event file. (This is equivalent to calling `add_graph()` later).

    TensorBoard will pick the graph from the file and display it graphically so
    you can interactively explore the graph you built. You will usually pass
    the graph from the session in which you launched it:

    ```python
    ...create a graph...
    # Launch the graph in a session.
    sess = tf.compat.v1.Session()
    # Create a summary writer, add the 'graph' to the event file.
    writer = tf.compat.v1.summary.FileWriter(<some-directory>, sess.graph)
    ```

    The `session` argument to the constructor makes the returned `FileWriter` a
    compatibility layer over new graph-based summaries (`tf.summary`).
    Crucially, this means the underlying writer resource and events file will
    be shared with any other `FileWriter` using the same `session` and `logdir`.
    In either case, ops will be added to `session.graph` to control the
    underlying file writer resource.

    Args:
      logdir: A string. Directory where event file will be written.
      graph: A `Graph` object, such as `sess.graph`.
      max_queue: Integer. Size of the queue for pending events and summaries.
      flush_secs: Number. How often, in seconds, to flush the
        pending events and summaries to disk.
      graph_def: DEPRECATED: Use the `graph` argument instead.
      filename_suffix: A string. Every event file's name is suffixed with
        `suffix`.
      session: A `tf.compat.v1.Session` object. See details above.

    Raises:
      RuntimeError: If called with eager execution enabled.

    @compatibility(eager)
      `v1.summary.FileWriter` is not compatible with eager execution.
      To write TensorBoard summaries under eager execution,
      use `tf.summary.create_file_writer` or
      a `with v1.Graph().as_default():` context.
    @end_compatibility
    """
if context.executing_eagerly():
    raise RuntimeError(
        "v1.summary.FileWriter is not compatible with eager execution. "
        "Use `tf.summary.create_file_writer`,"
        "or a `with v1.Graph().as_default():` context")
if session is not None:
    event_writer = EventFileWriterV2(
        session, logdir, max_queue, flush_secs, filename_suffix)
else:
    event_writer = EventFileWriter(logdir, max_queue, flush_secs,
                                   filename_suffix)

self._closed = False
super(FileWriter, self).__init__(event_writer, graph, graph_def)
