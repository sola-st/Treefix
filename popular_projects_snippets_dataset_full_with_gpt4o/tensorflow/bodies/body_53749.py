# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if async_mode:
    with context.execution_mode(context.ASYNC):
        f(self, *args, **kwargs)
else:
    with context.execution_mode(context.SYNC):
        f(self, *args, **kwargs)
