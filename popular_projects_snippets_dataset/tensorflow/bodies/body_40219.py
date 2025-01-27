# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/custom_device_test.py
device_name = '/job:localhost/replica:0/task:0/device:CUSTOM:0'
device, device_info, arrived_flag, executed_flag = (
    custom_device_testutil.GetLoggingDeviceCapsules(device_name))
context.register_custom_device(device, device_name, device_info)
self.assertFalse(custom_device_testutil.FlagValue(arrived_flag))
self.assertFalse(custom_device_testutil.FlagValue(executed_flag))
with ops.device(device_name):
    x = constant_op.constant(1.)
    y = x * constant_op.constant(2.)
self.assertTrue(custom_device_testutil.FlagValue(executed_flag))
# There was no copy onto the device. Actually I'm not sure how to trigger
# that from Python.
self.assertFalse(custom_device_testutil.FlagValue(arrived_flag))
with self.assertRaisesRegex(errors.InternalError, 'Trying to copy'):
    y.numpy()
