# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer_v2.py
"""Creates an `EventFileWriterV2` and an event file to write to.

    On construction, this calls `tf.contrib.summary.create_file_writer` within
    the graph from `session.graph` to look up a shared summary writer resource
    for `logdir` if one exists, and create one if not. Creating the summary
    writer resource in turn creates a new event file in `logdir` to be filled
    with `Event` protocol buffers passed to `add_event`. Graph ops to control
    this writer resource are added to `session.graph` during this init call;
    stateful methods on this class will call `session.run()` on these ops.

    Note that because the underlying resource is shared, it is possible that
    other parts of the code using the same session may interact independently
    with the resource, e.g. by flushing or even closing it. It is the caller's
    responsibility to avoid any undesirable sharing in this regard.

    The remaining arguments to the constructor (`flush_secs`, `max_queue`, and
    `filename_suffix`) control the construction of the shared writer resource
    if one is created. If an existing resource is reused, these arguments have
    no effect.  See `tf.contrib.summary.create_file_writer` for details.

    Args:
      session: A `tf.compat.v1.Session`. Session that will hold shared writer
        resource. The writer ops will be added to session.graph during this
        init call.
      logdir: A string. Directory where event file will be written.
      max_queue: Integer. Size of the queue for pending events and summaries.
      flush_secs: Number. How often, in seconds, to flush the
        pending events and summaries to disk.
      filename_suffix: A string. Every event file's name is suffixed with
        `filename_suffix`.
    """
self._session = session
self._logdir = logdir
self._closed = False
gfile.MakeDirs(self._logdir)

with self._session.graph.as_default():
    with ops.name_scope('filewriter'):
        file_writer = summary_ops_v2.create_file_writer(
            logdir=self._logdir,
            max_queue=max_queue,
            flush_millis=flush_secs * 1000,
            filename_suffix=filename_suffix)
        with summary_ops_v2.always_record_summaries(), file_writer.as_default():
            self._event_placeholder = array_ops.placeholder_with_default(
                constant_op.constant('unused', dtypes.string),
                shape=[])
            self._add_event_op = summary_ops_v2.import_event(
                self._event_placeholder)
        self._init_op = file_writer.init()  # pylint: disable=assignment-from-no-return
        self._flush_op = file_writer.flush()  # pylint: disable=assignment-from-no-return
        self._close_op = file_writer.close()  # pylint: disable=assignment-from-no-return
    self._session.run(self._init_op)
