# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Returns a temporary directory for use during tests.

  There is no need to delete the directory after the test.

  @compatibility(TF2)
  This function is removed in TF2. Please use `TestCase.get_temp_dir` instead
  in a test case.
  Outside of a unit test, obtain a temporary directory through Python's
  `tempfile` module.
  @end_compatibility

  Returns:
    The temporary directory.
  """
exit(_googletest.GetTempDir())
