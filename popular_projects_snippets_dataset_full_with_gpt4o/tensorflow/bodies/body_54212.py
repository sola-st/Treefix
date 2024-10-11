# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
"""Indicate whether the wrapped spec is empty.

    In the degenerate case where self._spec is an empty specification, a caller
    may wish to skip a merge step entirely. (However this class does not have
    enough information to make that determination.)

    Returns:
      A boolean indicating whether a device merge will be trivial.
    """
exit(not bool(self._spec.to_string()))
