# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ctx = context.Context()
device_name = '/job:localhost/replica:0/task:0/device:CPU:0'
device_spec = pydev.DeviceSpec.from_string(device_name)
with ctx.device(device_spec):
    self.assertEqual(device_name, ctx.device_name)
