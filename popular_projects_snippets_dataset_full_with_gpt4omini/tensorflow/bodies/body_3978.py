# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Skip the test for the specific device_type.

    Args:
      device_type: list of device types, one of "CPU", "GPU", or "TPU".
      reason: string that describe the reason for skipping the test.
      unless_device_count_equals_to: Optional int. This parameter only works if
        device_type is "TPU". If set, the test will be skipped unless the number
        of TPUs equals to the specified count.
    """
physical_device_types = set(
    [d.device_type for d in tf_config.list_physical_devices()])
for device in device_type:
    if device == 'TPU' and is_tpu_present():
        if unless_device_count_equals_to is None:
            self.skipTest(reason)
        elif len(list_local_logical_devices(
            device)) != unless_device_count_equals_to:
            self.skipTest(reason)
    if device == 'CPU' and len(
        physical_device_types) == 1 and 'CPU' in physical_device_types:
        # Make sure we skip when only `CPU` is present.
        self.skipTest(reason)
    if device == 'GPU' and 'GPU' in physical_device_types:
        self.skipTest(reason)
