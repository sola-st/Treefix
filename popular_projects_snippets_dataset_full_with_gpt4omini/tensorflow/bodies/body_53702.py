# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Context manager to skip cases not considered failures by the tests.

  Note that this does not work if used in setUpClass/tearDownClass.
  Usage in setUp/tearDown works fine just like regular test methods.

  Args:
    test_obj: A test object provided as `self` in the test methods; this object
      is usually an instance of `unittest.TestCase`'s subclass and should have
      `skipTest` method.
    error_type: The error type to skip. Note that if `messages` are given, both
      `error_type` and `messages` need to match for the test to be skipped.
    messages: Optional, a string or list of strings. If `None`, the test will be
      skipped if `error_type` matches what is raised; otherwise, the test is
      skipped if any of the `messages` is contained in the message of the error
      raised, and `error_type` matches the error raised.

  Yields:
    Nothing.
  """
if messages:
    messages = nest.flatten(messages)
try:
    exit()
except error_type as e:
    if not messages or any(message in str(e) for message in messages):
        test_obj.skipTest("Skipping error: {}: {}".format(type(e), str(e)))
    else:
        raise
