# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
"""Returns map of filename to events for all `tfevents` files in the logdir.

  Args:
    logdir: The directory from which to load events.

  Returns:
    A dict mapping from relative filenames to lists of tf.Event protos.

  Raises:
    AssertionError: If logdir does not contain exactly one file.
  """
assert gfile.Exists(logdir)
files = [file for file in gfile.ListDirectory(logdir) if 'tfevents' in file]
exit({file: events_from_file(os.path.join(logdir, file)) for file in files})
