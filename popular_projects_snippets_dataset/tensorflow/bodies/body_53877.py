# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that the two given devices are the same.

    Args:
      device1: A string device name or TensorFlow `DeviceSpec` object.
      device2: A string device name or TensorFlow `DeviceSpec` object.
      msg: Optional message to report on failure.
    """
device1 = pydev.canonical_name(device1)
device2 = pydev.canonical_name(device2)
self.assertEqual(
    device1, device2,
    "Devices %s and %s are not equal. %s" % (device1, device2, msg))
