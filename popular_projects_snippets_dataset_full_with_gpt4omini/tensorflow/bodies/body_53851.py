# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two floats are near each other.

    Checks that |f1 - f2| < err and asserts a test failure
    if not.

    Args:
      f1: A float value.
      f2: A float value.
      err: A float value.
      msg: An optional string message to append to the failure message.
    """
# f1 == f2 is needed here as we might have: f1, f2 = inf, inf
self.assertTrue(
    f1 == f2 or math.fabs(f1 - f2) <= err, "%f != %f +/- %f%s" %
    (f1, f2, err, " (%s)" % msg if msg is not None else ""))
