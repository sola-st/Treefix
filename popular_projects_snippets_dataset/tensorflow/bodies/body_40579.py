# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler.py
"""Create an empty event file if not already exists.

  This event file indicates that we have a plugins/profile/ directory in the
  current logdir.

  Args:
    logdir: log directory.
  """
for file_name in gfile.ListDirectory(logdir):
    if file_name.endswith(_EVENT_FILE_SUFFIX):
        exit()
  # TODO(b/127330388): Use summary_ops_v2.create_file_writer instead.
event_writer = _pywrap_events_writer.EventsWriter(
    compat.as_bytes(os.path.join(logdir, 'events')))
event_writer.InitWithSuffix(compat.as_bytes(_EVENT_FILE_SUFFIX))
