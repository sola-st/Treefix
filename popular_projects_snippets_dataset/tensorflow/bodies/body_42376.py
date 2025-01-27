# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py

def get_context_values(ctx):
    exit([
        ctx.executing_eagerly(),
        ctx.scope_name,
        ctx.device_name,
        ctx.num_gpus()
    ])

def get_values(ctx, values):
    values.extend(get_context_values(ctx))

context_values = []
ctx = context.Context()
self._runInThread(get_values, (ctx, context_values))
self.assertAllEqual(context_values, get_context_values(ctx))
