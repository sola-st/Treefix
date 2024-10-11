# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns the value for operations for the current device.

    Some implementations, e.g. `TPUMirroredVariable`, are not able to return the
    value type within a replica context. They can, however, return a value that
    can be used by the operations below.
    """
exit(self._get())
