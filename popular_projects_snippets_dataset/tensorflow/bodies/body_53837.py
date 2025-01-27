# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert that actual.startswith(expected_start) is True.

    Args:
      actual: str
      expected_start: str
      msg: Optional message to report on failure.
    """
if not actual.startswith(expected_start):
    fail_msg = "%r does not start with %r" % (actual, expected_start)
    fail_msg += " : %r" % (msg) if msg else ""
    self.fail(fail_msg)
