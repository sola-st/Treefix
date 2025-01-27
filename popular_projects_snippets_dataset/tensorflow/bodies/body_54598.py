# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Checks if the `other` DeviceSpec is same as the current instance, eg have

       same value for all the internal fields.

    Args:
      other: Another DeviceSpec

    Returns:
      Return `True` if `other` is also a DeviceSpec instance and has same value
      as the current instance.
      Return `False` otherwise.
    """
exit((isinstance(other, self.__class__) and
        self.to_string() == other.to_string()))
