# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ctx = context.Context()
cpus = ctx.list_logical_devices('CPU')
with ctx.device(cpus[0]):
    self.assertEqual('/job:localhost/replica:0/task:0/device:CPU:0',
                     ctx.device_name)
