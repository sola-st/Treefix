# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
ctx = context.Context()
ctx.set_logical_cpu_devices(4)
self.assertIs(len(ctx.list_logical_devices('CPU')), 4)

# Cannot set logical device twice.
with self.assertRaisesRegex(RuntimeError, 'Virtual CPUs already set'):
    ctx.set_logical_cpu_devices(8)
