# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Creates a `EventFileWriter` and an event file to write to.

    On construction the summary writer creates a new event file in `logdir`.
    This event file will contain `Event` protocol buffers, which are written to
    disk via the add_event method.

    The other arguments to the constructor control the asynchronous writes to
    the event file:

    *  `flush_secs`: How often, in seconds, to flush the added summaries
       and events to disk.
    *  `max_queue`: Maximum number of summaries or events pending to be
       written to disk before one of the 'add' calls block.

    Args:
      logdir: A string. Directory where event file will be written.
      max_queue: Integer. Size of the queue for pending events and summaries.
      flush_secs: Number. How often, in seconds, to flush the
        pending events and summaries to disk.
      filename_suffix: A string. Every event file's name is suffixed with
        `filename_suffix`.
    """
self._logdir = str(logdir)
gfile.MakeDirs(self._logdir)
self._max_queue = max_queue
self._flush_secs = flush_secs
self._flush_complete = threading.Event()
self._flush_sentinel = object()
self._close_sentinel = object()
self._ev_writer = _pywrap_events_writer.EventsWriter(
    compat.as_bytes(os.path.join(self._logdir, "events")))
if filename_suffix:
    self._ev_writer.InitWithSuffix(compat.as_bytes(filename_suffix))
self._initialize()
self._closed = False
