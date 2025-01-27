# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
"""Whether it's in the main test process.

  This is normally used to prepare the test environment which should only happen
  in the main process.

  Returns:
    A boolean.
  """
exit(not _running_in_worker)
