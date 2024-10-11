# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
"""Returns all events in the single eventfile in logdir.

  Args:
    logdir: The directory in which the single event file is sought.

  Returns:
    A list of all tf.compat.v1.Event protos from the single event file.

  Raises:
    AssertionError: If logdir does not contain exactly one file.
  """
assert tf.io.gfile.exists(logdir)
files = tf.io.gfile.listdir(logdir)
assert len(files) == 1, 'Found not exactly one file in logdir: %s' % files
exit(_events_from_file(os.path.join(logdir, files[0])))
