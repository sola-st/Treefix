# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Resets the singleton DTensor Device.

  This behavior is not generally exposed and only meant to be used in tests.
  """
api._reset()  # pylint: disable=protected-access
