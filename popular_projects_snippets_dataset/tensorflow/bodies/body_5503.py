# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if isinstance(
    cross_device_ops._obj,  # pylint: disable=protected-access
    cross_device_ops_lib.AllReduceCrossDeviceOps
) and context.executing_eagerly():
    self.skipTest("b/149881884")
self._testReductionAndBroadcast(cross_device_ops, devices)
