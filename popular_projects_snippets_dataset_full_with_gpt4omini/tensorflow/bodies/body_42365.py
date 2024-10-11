# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ctx = context.Context()
self.assertTrue(ctx.executing_eagerly())

self.assertEqual('', ctx.scope_name)
ctx.scope_name = 'foo'
self.assertEqual('foo', ctx.scope_name)

self.assertEqual(context.SYNC, ctx.execution_mode)
ctx.execution_mode = context.ASYNC
self.assertEqual(context.ASYNC, ctx.execution_mode)
ctx.execution_mode = context.SYNC
self.assertEqual(context.SYNC, ctx.execution_mode)

self.assertEqual('', ctx.device_name)
self.assertEqual(ctx.device_name, ctx.device_spec.to_string())
with ctx.device('GPU:0'):
    self.assertEqual('/job:localhost/replica:0/task:0/device:GPU:0',
                     ctx.device_name)
    self.assertEqual(ctx.device_name, ctx.device_spec.to_string())
    with ctx.device(None):
        self.assertEqual('', ctx.device_name)
        self.assertEqual(ctx.device_name, ctx.device_spec.to_string())
        with ctx.device('CPU:0'):
            self.assertEqual('/job:localhost/replica:0/task:0/device:CPU:0',
                             ctx.device_name)
            self.assertEqual(ctx.device_name, ctx.device_spec.to_string())
        with ctx.device(ctx.list_logical_devices('CPU')[0]):
            self.assertEqual('/job:localhost/replica:0/task:0/device:CPU:0',
                             ctx.device_name)
            self.assertEqual(ctx.device_name, ctx.device_spec.to_string())

gpus = ctx.list_logical_devices('GPU')
if gpus:
    with ctx.device(gpus[0]):
        self.assertEqual('/job:localhost/replica:0/task:0/device:GPU:0',
                         ctx.device_name)
        self.assertEqual(ctx.device_name, ctx.device_spec.to_string())

has_cpu_device = False
for x in ctx.devices():
    has_cpu_device = has_cpu_device or 'CPU' in x
self.assertTrue(has_cpu_device)
del ctx
