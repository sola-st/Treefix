# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
"""Returns all events in the single eventfile in logdir.

  Args:
    logdir: The directory in which the single event file is sought.

  Returns:
    A list of all tf.Event protos from the single event file.

  Raises:
    AssertionError: If logdir does not contain exactly one file.
  """
assert gfile.Exists(logdir)
files = gfile.ListDirectory(logdir)
assert len(files) == 1, 'Found not exactly one file in logdir: %s' % files
exit(events_from_file(os.path.join(logdir, files[0])))
