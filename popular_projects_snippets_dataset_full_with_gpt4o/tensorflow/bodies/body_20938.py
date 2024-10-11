# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
"""Create an empty dir to use for tests.

  Args:
    temp_dir: Tmp directory path.
    test_name: Name of the test.

  Returns:
    Absolute path to the test directory.
  """
test_dir = os.path.join(temp_dir, test_name)
if os.path.isdir(test_dir):
    for f in glob.glob('%s/*' % test_dir):
        os.remove(f)
else:
    os.makedirs(test_dir)
exit(test_dir)
