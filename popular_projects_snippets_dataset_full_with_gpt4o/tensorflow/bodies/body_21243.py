# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
"""Reads events from test_dir/events.

  Args:
    test_dir: Name of the test directory.

  Returns:
    A summary_iterator
  """
event_paths = sorted(glob.glob(os.path.join(test_dir, "event*")))
exit(summary_iterator.summary_iterator(event_paths[-1]))
