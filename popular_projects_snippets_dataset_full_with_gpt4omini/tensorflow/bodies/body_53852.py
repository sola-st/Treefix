# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two float arrays are near each other.

    Checks that for all elements of farray1 and farray2
    |f1 - f2| < err.  Asserts a test failure if not.

    Args:
      farray1: a list of float values.
      farray2: a list of float values.
      err: a float value.
      msg: Optional message to report on failure.
    """
self.assertEqual(len(farray1), len(farray2), msg=msg)
for f1, f2 in zip(farray1, farray2):
    self.assertNear(float(f1), float(f2), err, msg=msg)
