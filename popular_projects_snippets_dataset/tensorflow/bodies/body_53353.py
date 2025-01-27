# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Dummy method to prevent a tensor from being used as a Python `bool`.

    This is the Python 2.x counterpart to `__bool__()` above.

    Raises:
      `TypeError`.
    """
self._disallow_bool_casting()
