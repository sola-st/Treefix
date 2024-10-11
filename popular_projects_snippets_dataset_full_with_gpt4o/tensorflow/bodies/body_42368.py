# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ctx = context.Context(execution_mode=context.ASYNC)
ctx.ensure_initialized()
has_cpu_device = False
for x in ctx.devices():
    has_cpu_device = has_cpu_device or 'CPU' in x
self.assertTrue(has_cpu_device)
del ctx
