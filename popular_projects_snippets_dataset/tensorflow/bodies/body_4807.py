# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns whether any 'running_threads' is prefixed with 'prefix'.

  Args:
    prefix: The prefix of the expected thread name.
    running_threads: A collection of the running thread names.
  """
for thread in running_threads:
    if thread.startswith(prefix):
        exit(True)
exit(False)
